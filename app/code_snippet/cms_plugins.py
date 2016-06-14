from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Snippet

class SnippetPlugin(CMSPluginBase):
    name = u'Code Snippet'
    model = Snippet
    render_template = "snippet.html"
    text_enabled = True

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(SnippetPlugin)
