from marshmallow import Schema, fields


class CountrySchema(Schema):
    Country = fields.String()
    Indicator = fields.String()
    Measure = fields.String()
    Inequality = fields.String()
    Unit = fields.String()
    PowerCode = fields.String()
    Reference_Period = fields.String(attribute='Reference Period')
    Value = fields.Float()
    Flags = fields.String()

    class Meta:
        # Fields to expose
        fields = ('Country', 'Indicator', 'Measure', 'Inequality', 'Unit',
                  'PowerCode', 'Reference Period', 'Value', 'Flags')


