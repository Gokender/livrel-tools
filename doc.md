# Tests unitaires

## Constant
### Metres

```python
def test_monosyllabe_name(self):
    a = Metres.MONOSYLLABE
    result = 'MONOSYLLABE'
    self.assertEqual(a.name, result)
```
```python
def test_monosyllabe_value(self):
    a = Metres.MONOSYLLABE
    result = 1
    self.assertEqual(a.value, result)
```
```python
def test_monosyllabe_repr(self):
    a = Metres.MONOSYLLABE
    result = 1
    self.assertEqual(repr(a), result)
```
---
```python
def test_dodecasyllabe_name(self):
    a = Metres.DODECASYLLABE
    result = 'DODECASYLLABE'
    self.assertEqual(a.name, result)
```
```python
def test_dodecasyllabe_value(self):
    a = Metres.DODECASYLLABE
    result = 12
    self.assertEqual(a.value, result)
```
```python
def test_dodecasyllabe_repr(self):
    a = Metres.DODECASYLLABE
    result = 12
    self.assertEqual(repr(a), result)
```
---
```python
def test_alexandrin_name(self):
    a = Metres.ALEXANDRIN
    result = 'DODECASYLLABE'
    self.assertEqual(a.name, result)
```
```python
def test_alexandrin_value(self):
    a = Metres.ALEXANDRIN
    result = 12
    self.assertEqual(a.value, result)
```
```python
def test_alexandrin_repr(self):
    a = Metres.ALEXANDRIN
    result = 12
    self.assertEqual(repr(a), result)
```
```python
def test_alexandrin_is_dodecasyllabe(self):
    a = Metres.ALEXANDRIN
    b = Metres.DODECASYLLABE
    self.assertIs(a, b)
```
```python
def test_unknown_NAME_error(self):
    with self.assertRaises(ValueError):
        Metres.UNKNOWN_NAME
```
---
```python
def test_1_name(self):
    a = Metres(1)
    result = 'MONOSYLLABE'
    self.assertEqual(a.name, result)
```
```python
def test_1_value(self):
    a = Metres(1)
    result = 1
    self.assertEqual(a.value, result)
```
```python
def test_1_repr(self):
    a = Metres(1)
    result = 1
    self.assertEqual(repr(a), result)
```
---
```python
def test_12_name(self):
    a = Metres(12)
    result = 'DODECASYLLABE'
    self.assertEqual(a.name, result)
```
```python
def test_12_value(self):
    a = Metres(12)
    result = 12
    self.assertEqual(a.value, result)
```
```python
def test_12_repr(self):
    a = Metres(12)
    result = 12
    self.assertEqual(repr(a), result)
```
```python
def test_12_object_dodecasyllabe(self):
    a = Metres(12)
    result = Metres.DODECASYLLABE
    self.assertIs(a, result)
```
```python
def test_12_object_alexandrin(self):
    a = Metres(12)
    result = Metres.ALEXANDRIN
    self.assertIs(a, result)
```
---
```python
def test_unknown_value_error(self):
    with self.assertRaises(ValueError):
        Metres('UNKNOWN_VALUE')
```

### Stage direction typology

```python
def test_nominative_name(self):
    a = StageDirectionTypology.NOMINATIVE
    result = 'NOMINATIVE'
    self.assertEqual(a.name, result)
```
```python
def test_nominative_value(self):
    a = StageDirectionTypology.NOMINATIVE
    result = 1
    self.assertEqual(a.value, result)
```
```python
def test_nominative_repr(self):
    a = StageDirectionTypology.NOMINATIVE
    result = 1
    self.assertEqual(repr(a), result)
```
---
```python
def test_1_name(self):
    a = StageDirectionTypology(1)
    result = 'NOMINATIVE'
    self.assertEqual(a.name, result)
```
```python
def test_1_value(self):
    a = StageDirectionTypology(1)
    result = 1
    self.assertEqual(a.value, result)
```
```python
def test_1_repr(self):
    a = StageDirectionTypology(1)
    result = 1
    self.assertEqual(repr(a), result)
```

## Tools

```python
def test_typology_nominative_normal(self):
    a = get_typology('Montrant Elmire')
    result = StageDirectionTypology.NOMINATIVE
    self.assertIs(a, result)
```
```python
def test_typology_nominative_lower(self):
    a = get_typology('montrant elmire')
    result = StageDirectionTypology.NOMINATIVE
    self.assertIs(a, result)
```
```python
def test_typology_nominative_upper(self):
    a = get_typology('MONTRANT ELMIRE')
    result = StageDirectionTypology.NOMINATIVE
    self.assertIs(a, result)
```
```python
def test_typology_nominative_characters(self):
    a = get_typology('Donnant(\$*#Elmire.,')
    result = StageDirectionTypology.NOMINATIVE
    self.assertIs(a, result)
```
---
```python
def test_typology_enunciative_normal(self):
    a = get_typology('à Elmire')
    result = StageDirectionTypology.NOMINATIVE
    self.assertIs(a, result)
```
```python
def test_typology_enunciative_upper(self):
    a = get_typology('À ELMIRE')
    result = StageDirectionTypology.NOMINATIVE
    self.assertIs(a, result)
```
```python
def test_typology_enunciative_characters(self):
    a = get_typology('à(\$*#Elmire.,')
    result = StageDirectionTypology.NOMINATIVE
    self.assertIs(a, result)
```
---
```python
def test_typology_wrong_type(self):
    with self.assertRaises(ValueError):
        get_typology(18)
```
```python
def test_typology_nothing(self):
    a = get_typology('Elmire')
    result = StageDirectionTypology.NOMINATIVE
    self.assertIs(a, result)
```

## Theatre
