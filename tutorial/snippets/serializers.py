from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User



class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedIdentityField(many=True, view_name='snippet_detail')

    class Meta:
        model = User
        fields = ('url', 'username', 'snippets')


#the old way 
#class SnippetSerializer(serializers.Serializer):
#    pk = serializers.Field()  # Note: 'Field' is an untyped read-only field.
#    title = serializers.CharField(required=False,
#                                  max_length=100)
#    code = serializers.CharField(widget=widgets.Textarea,
#                                 max_length=100000)
#    linenos= serializers.BooleanField(required=False)
#    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,
#                                 default='python')
#    style = serializers.ChoiceField(choices=STYLE_CHOICES,
#                                    default='friendly')
#    # updated this to reflect the snippets association with the users
#    owner = serializers.Field(source='owner.username')
#
#    def restore_object(self, attrs, instance=None):
#        """
#        Create or update a new snippet instance, given a dictionary
#        of deserialized field values.STYLE_CHOICES
#        Note that if we don't define this method, then deserializing
#        data will simple return a dictionary of items.
#        """
#        if instance:
#            # Update existing instance
#            instance.title = attrs.get('title', instance.title)
#            instance.code = attrs.get('code', instance.code)
#            instance.linenos = attrs.get('linenos', instance.linenos)
#            instance.language = attrs.get('language',instance.language)
#            instance.style= attrs.get('style', instance.style)
#            return instance
#
#        # Create a new instance
#        return Snippet(**attrs)
#
#
#class UserSerializer(serializers.ModelSerializer):
#    snippets = serializers.PrimaryKeyRelatedField(many=True)
#
#
#    # make sure that you also add the 'owner' to the meta class fields
#    # was wrong here this needs to be a sub class
#    # the meta class gives you options as to what data you want shown
#    class Meta:
#        model = User
#        fields = ('id', 'username', 'snippets')