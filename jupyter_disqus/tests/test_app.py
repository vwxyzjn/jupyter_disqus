from jupyter_disqus.app import _format_disqus_code
from unittest.mock import MagicMock

def test_format_disqus_code():
    assert _format_disqus_code(
        page_url="https://costahuang.me",
        page_identifier="SC2AI/",
        site_shortname="costahuang"
    ) == " <div id=disqus_thread></div> <script>\n\n    /**\n    *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.\n    *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/\n\n    var disqus_config = function () {\n    this.page.url = 'https://costahuang.me';  // Replace PAGE_URL with your page's canonical URL variable\n    this.page.identifier = 'SC2AI/'; // Replace PAGE_IDENTIFIER with your page's unique identifier variable\n    };\n    (function() { // DON'T EDIT BELOW THIS LINE\n    var d = document, s = d.createElement('script');\n    s.src = 'https://costahuang.disqus.com/embed.js';\n    s.setAttribute('data-timestamp', +new Date());\n    (d.head || d.body).appendChild(s);\n    })();\n    </script> <noscript>Please enable JavaScript to view the <a href=https://disqus.com/?ref_noscript>comments powered by Disqus.</a></noscript> <script id=dsq-count-scr src=//costahuang.disqus.com/count.js async></script> </body> "