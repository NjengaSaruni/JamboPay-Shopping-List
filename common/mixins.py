import operator

from django.db.models import Q
from rest_framework import serializers


class GetQuerysetBaseMixin(object):
    def get_queryset(self, *args, **kwargs):
        self.queryset = super(GetQuerysetBaseMixin, self).get_queryset(*args, **kwargs)

        query = self.request.GET.get("q") or False
        # An icontains search using values in search fields specified in the calling view

        if query and hasattr(self, 'search_fields'):
            fields = [(field + '__icontains', query) for field in self.search_fields]

            q_list = [Q(x) for x in fields]

            self.queryset = self.queryset.filter(
                reduce(operator.or_, q_list)
            )

            self.queryset = self.queryset.distinct()

        return self.queryset


class GetQuerysetMixin(GetQuerysetBaseMixin):
    user = None

    def filter_by_shopper(self):
        """
            Tries to get the institution to which a given object belongs
        """

        return self.queryset.filter(
            shopper__id=self.request.user.id
        ).exclude(
            shopper=None
        )

    def get_queryset(self, *args, **kwargs):
        self.queryset = super(GetQuerysetMixin, self).get_queryset(*args, **kwargs)

        self.user = self.request.user

        self.queryset = self.filter_by_shopper()

        return self.queryset


class AbstractFieldsMixin(serializers.ModelSerializer):
    # Use this method for the custom field
    def _user(self):
        request = getattr(self.context, 'request', None)
        if request:
            return request.user

    def create(self, validated_data):
        user = self._user()

        self.initial_data['shopper'] = user.id

        print self.initial_data

        return super(AbstractFieldsMixin, self).create(validated_data)
