from IPython.display import HTML
import IPython
import htmlmin

def _format_disqus_code(page_url: str, page_identifier: str, site_shortname: str) -> str:
    """This function formats the necessary html and javascript codes needed to be
    inserted into the jupyter notebook

    Args:
        page_url (str): your page's canonical URL
        page_identifier (str): your page's unique identifier
        site_shortname (str): your site's disqus shortname

    Returns:
        str: the formatted html disqus code

    """
    disqus_code = """
    <div id="disqus_thread"></div>
    <script>

    /**
    *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
    *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/

    var disqus_config = function () {
    this.page.url = '%s';  // Replace PAGE_URL with your page's canonical URL variable
    this.page.identifier = '%s'; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
    };
    (function() { // DON'T EDIT BELOW THIS LINE
    var d = document, s = d.createElement('script');
    s.src = 'https://%s.disqus.com/embed.js';
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
    })();
    </script>
    <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
        <script id="dsq-count-scr" src="//%s.disqus.com/count.js" async></script>
    </body>
    """ % (page_url, page_identifier, site_shortname, site_shortname)

    return htmlmin.minify(disqus_code)

def inject(page_url: str, page_identifier: str, site_shortname: str) -> IPython.core.display.HTML:
    """this function injects and displays a disqus commenting section in a code cell of your jupyter notebook
    Args:
        page_url (str): your page's canonical URL
        page_identifier (str): your page's unique identifier
        site_shortname (str): your site's disqus shortname

    Returns:
        IPython.core.display.HTML

    Example:
        >>> from jupyter_disqus import inject
        >>> # call this function in a separate code cell of your jupyter notebook
        >>> inject(
                page_url="https://costahuang.me/SC2AI/",
                page_identifier="1f527ae5-5a59-4dc3-9bb0-d77c2ccf5cab",
                site_shortname="costahuang"
            )
    """
    return HTML(_format_disqus_code(page_url, page_identifier, site_shortname))
