from jupyter_disqus import inject
from unittest.mock import MagicMock

def test_inject():
    assert inject(
        page_url="https://costahuang.me",
        page_identifier="SC2AI/",
        site_shortname="costahuang"
    ) == "<div id=disqus_thread></div> <script>\n\n/**\n*  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.\n*  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/\n\nvar disqus_config = function () {\nthis.page.url = 'https://costahuang.me';  // Replace PAGE_URL with your page's canonical URL variable\nthis.page.identifier = 'SC2AI/'; // Replace PAGE_IDENTIFIER with your page's unique identifier variable\n};\n(function() { // DON'T EDIT BELOW THIS LINE\nvar d = document, s = d.createElement('script');\ns.src = 'https://costahuang.disqus.com/embed.js';\ns.setAttribute('data-timestamp', +new Date());\n(d.head || d.body).appendChild(s);\n})();\n</script> <noscript>Please enable JavaScript to view the <a href=https://disqus.com/?ref_noscript>comments powered by Disqus.</a></noscript> <script id=dsq-count-scr src=//costahuang.disqus.com/count.js async></script> </body> "
