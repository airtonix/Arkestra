from widgetry import fk_lookup
from django.db.models import ForeignKey


class AutocompleteMixin(object):
    class Media:
        js = (
            '/static/jquery/jquery.js', # we already load jquery for the tabs
            '/static/jquery/ui/ui.core.js',
            '/static/jquery/ui/ui.tabs.js',
        )
        css = {
            'all': ('/static/jquery/themes/base/ui.all.css',)
        }    

    def formfield_for_dbfield(self, db_field, **kwargs):
        """
        Overrides the default widget for Foreignkey fields if they are
        specified in the related_search_fields class attribute.
        """
        if (isinstance(db_field, ForeignKey) and 
                db_field.name in self.related_search_fields):
            kwargs['widget'] = fk_lookup.FkLookup(db_field.rel.to)
        return super(AutocompleteMixin, self).formfield_for_dbfield(db_field, **kwargs)

class SupplyRequestMixin(object):
    def get_form(self, request, obj=None, **kwargs):
        form_class = super(SupplyRequestMixin, self).get_form(request, obj, **kwargs)
        form_class.request = request
        return form_class