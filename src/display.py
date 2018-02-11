# Copyright 2018 Cedric Canovas

from IPython.display import HTML, display
from string import Template
import json
import uuid

def init(version="4.13.0"):
    display(HTML('''<script>
requirejs.config({
    paths: {
        d3: "//cdnjs.cloudflare.com/ajax/libs/d3/'''+version+'''/d3"
    }
});
require(['d3'], function(d3) {
    window.d3 = d3;
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
        'data': df.to_json(orient='records'),
        'params': json.dumps(params),
        'width': width,
        'height': height
    })))
