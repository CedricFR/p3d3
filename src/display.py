# Copyright 2018 Cedric Canovas

from IPython.display import HTML, display
from string import Template
import json
import uuid
from .util import sanitize, P3JsonEncoder

def init(version="4.13.0"):
    display(HTML('''<script>
requirejs.config({
    paths: {
        d3: "//cdnjs.cloudflare.com/ajax/libs/d3/'''+version+'''/d3",
        vg: "https://cdn.jsdelivr.net/npm/vega@3.0.10?noext",
        vl: "https://cdn.jsdelivr.net/npm/vega-lite@2.1.3?noext",
        vg_embed: "https://cdn.jsdelivr.net/npm/vega-embed@3.0.0?noext"
    },
    shim: {
        vg_embed: {deps: ["vg.global", "vl.global"]},
        vl: {deps: ["vg"]},
        vg: {deps: ["d3"]}
    }
});
require(['d3'], function(d3) {
    window.d3 = d3;
});

define('vg.global', ['vg'], function(vgGlobal) {
    window.vega = vgGlobal;
});

define('vl.global', ['vl'], function(vlGlobal) {
    window.vl = vlGlobal;
});

require(["vg_embed"], function(vg_embed) {
    window.vg_embed = vg_embed;
});
</script>'''))

def p3d3(df, jsfile, params={}, width=800, height=500):
    script = ""
    with open(jsfile, 'r') as script_file:
        script = script_file.read()


    tmp = Template('''
        <svg id="$id"></svg>
        <script type="text/javascript">
	(function() {
        $script

        main(d3.select("#$id"), $data, $params, $width, $height);
        })();
        </script>''')

    display(HTML(tmp.substitute({
        'id': "a"+str(uuid.uuid4()),
        'script': script,
        'data': sanitize(df).to_json(orient='records'),
        'params': json.dumps(params, cls=P3JsonEncoder),
        'width': width,
        'height': height
    })))

def vegalite(df, specs):
    tmp = Template('''
        <div id="$id"></div>
        <script type="text/javascript">
            vg_embed("#$id", $specs, {actions: {source: false, editor: false} });

        </script>''')

    specifications = specs
    specifications['$schema'] = "https://vega.github.io/schema/vega-lite/v2.json"
    specifications['data'] = dict(values = sanitize(df).to_dict(orient='records'))
    if not 'width' in specifications:
        specifications['width'] = 800
    if not 'height' in specifications:
        specifications['height'] = 500

    display(HTML(tmp.substitute({
        'id': "a"+str(uuid.uuid4()),
        'specs': json.dumps(specifications, cls=P3JsonEncoder)
    })))
