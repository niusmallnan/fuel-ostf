#    Copyright 2013 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import json

from sqlalchemy.types import TypeDecorator
from sqlalchemy import String

class JsonField(TypeDecorator):
    impl = String

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)

        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value


class ListField(JsonField):
    def process_bind_param(self, value, dialect):
        value = list(value) if value else []
        return super(ListField, self).process_bind_param(value, dialect)

    def process_result_value(self, value, dialect):
        value = super(ListField, self).process_result_value(value, dialect)
        return list(value) if value else []
