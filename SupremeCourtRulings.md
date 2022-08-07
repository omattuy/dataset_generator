```python
import pandas as pd
crashes = pd.read_csv('supreme_court.csv')
```


```python

```


```python
crashes.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>3_judge_dc</th>
      <th>docket</th>
      <th>name</th>
      <th>citation.led</th>
      <th>citation.lexis</th>
      <th>citation.sct</th>
      <th>citation.us</th>
      <th>decision.authority</th>
      <th>decision.direction</th>
      <th>decision.dissent agrees</th>
      <th>...</th>
      <th>decision.case.disposition</th>
      <th>decision.case.unusual</th>
      <th>decision.date.day</th>
      <th>decision.date.full</th>
      <th>decision.date.month</th>
      <th>decision.date.year</th>
      <th>voting.majority assigner.id</th>
      <th>voting.majority assigner.name</th>
      <th>voting.majority writer.id</th>
      <th>voting.majority writer.name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>True</td>
      <td>24</td>
      <td>HALLIBURTON OIL WELL CEMENTING CO. v. WALKER e...</td>
      <td>91 L. Ed. 3</td>
      <td>1946 U.S. LEXIS 1724</td>
      <td>67 S. Ct. 6</td>
      <td>329 U.S. 1</td>
      <td>4.0</td>
      <td>liberal</td>
      <td>True</td>
      <td>...</td>
      <td>reversed</td>
      <td>True</td>
      <td>18</td>
      <td>11/18/1946</td>
      <td>11</td>
      <td>1946</td>
      <td>78</td>
      <td>HLBlack</td>
      <td>78</td>
      <td>HLBlack</td>
    </tr>
    <tr>
      <th>1</th>
      <td>True</td>
      <td>280</td>
      <td>FUNK BROTHERS SEED CO. v. KALO INOCULANT CO.</td>
      <td>92 L. Ed. 2d 588</td>
      <td>1948 U.S. LEXIS 2842</td>
      <td>68 S. Ct. 440</td>
      <td>333 U.S. 127</td>
      <td>7.0</td>
      <td>liberal</td>
      <td>True</td>
      <td>...</td>
      <td>reversed</td>
      <td>True</td>
      <td>16</td>
      <td>2/16/1948</td>
      <td>2</td>
      <td>1948</td>
      <td>87</td>
      <td>FMVinson</td>
      <td>81</td>
      <td>WODouglas</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>85</td>
      <td>YOUNG v. UNITED STATES ex rel. VUITTON ET FILS...</td>
      <td>95 L. Ed. 2d 740</td>
      <td>1987 U.S. LEXIS 2261</td>
      <td>107 S. Ct. 2124</td>
      <td>481 U.S. 787</td>
      <td>3.0</td>
      <td>liberal</td>
      <td>True</td>
      <td>...</td>
      <td>reversed</td>
      <td>True</td>
      <td>26</td>
      <td>5/26/1987</td>
      <td>5</td>
      <td>1987</td>
      <td>92</td>
      <td>WJBrennan</td>
      <td>92</td>
      <td>WJBrennan</td>
    </tr>
    <tr>
      <th>3</th>
      <td>True</td>
      <td>71</td>
      <td>UNITED STATES v. GLAXO GROUP LTD. et al.</td>
      <td>35 L. Ed. 2d 104</td>
      <td>1973 U.S. LEXIS 26</td>
      <td>93 S. Ct. 861</td>
      <td>410 U.S. 52</td>
      <td>7.0</td>
      <td>liberal</td>
      <td>True</td>
      <td>...</td>
      <td>reversed</td>
      <td>True</td>
      <td>22</td>
      <td>1/22/1973</td>
      <td>1</td>
      <td>1973</td>
      <td>99</td>
      <td>WEBurger</td>
      <td>95</td>
      <td>BRWhite</td>
    </tr>
    <tr>
      <th>4</th>
      <td>True</td>
      <td>250</td>
      <td>UNITED STATES v. NEW WRINKLE, INC. ET AL.</td>
      <td>96 L. Ed. 2d 417</td>
      <td>1952 U.S. LEXIS 2811</td>
      <td>72 S. Ct. 350</td>
      <td>342 U.S. 371</td>
      <td>4.0</td>
      <td>liberal</td>
      <td>True</td>
      <td>...</td>
      <td>reversed</td>
      <td>True</td>
      <td>4</td>
      <td>2/4/1952</td>
      <td>2</td>
      <td>1952</td>
      <td>87</td>
      <td>FMVinson</td>
      <td>79</td>
      <td>SFReed</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 56 columns</p>
</div>




```python
crashes.shape
```




    (8803, 56)




```python
crashes.columns
```




    Index(['3_judge_dc', 'docket', 'name', 'citation.led', 'citation.lexis',
           'citation.sct', 'citation.us', 'decision.authority',
           'decision.direction', 'decision.dissent agrees',
           'decision.jurisdiction', 'decision.precedent altered?', 'decision.term',
           'decision.type', 'decision.unconstitutional', 'decision.winning party',
           'id.case', 'id.case issues', 'id.docket', 'id.vote', 'issue.area',
           'issue.id', 'issue.text', 'laws.id', 'laws.type',
           'lower court.direction', 'lower court.disagreement?',
           'lower court.disposition', 'lower court.reasons', 'natural court.chief',
           'natural court.id', 'natural court.period', 'origin.id', 'origin.name',
           'source.id', 'source.name', 'voting.majority', 'voting.minority',
           'voting.split on second', 'voting.unclear',
           'arguments.petitioner.entity', 'arguments.petitioner.id',
           'arguments.respondent.entity', 'arguments.respondent.id',
           'decision.admin action.agency', 'decision.admin action.id',
           'decision.case.disposition', 'decision.case.unusual',
           'decision.date.day', 'decision.date.full', 'decision.date.month',
           'decision.date.year', 'voting.majority assigner.id',
           'voting.majority assigner.name', 'voting.majority writer.id',
           'voting.majority writer.name'],
          dtype='object')




```python
# Indexing by position
crashes_idx = crashes.iloc[:5,:]
```


```python
crashes_idx.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>3_judge_dc</th>
      <th>docket</th>
      <th>name</th>
      <th>citation.led</th>
      <th>citation.lexis</th>
      <th>citation.sct</th>
      <th>citation.us</th>
      <th>decision.authority</th>
      <th>decision.direction</th>
      <th>decision.dissent agrees</th>
      <th>...</th>
      <th>decision.case.disposition</th>
      <th>decision.case.unusual</th>
      <th>decision.date.day</th>
      <th>decision.date.full</th>
      <th>decision.date.month</th>
      <th>decision.date.year</th>
      <th>voting.majority assigner.id</th>
      <th>voting.majority assigner.name</th>
      <th>voting.majority writer.id</th>
      <th>voting.majority writer.name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>True</td>
      <td>24</td>
      <td>HALLIBURTON OIL WELL CEMENTING CO. v. WALKER e...</td>
      <td>91 L. Ed. 3</td>
      <td>1946 U.S. LEXIS 1724</td>
      <td>67 S. Ct. 6</td>
      <td>329 U.S. 1</td>
      <td>4.0</td>
      <td>liberal</td>
      <td>True</td>
      <td>...</td>
      <td>reversed</td>
      <td>True</td>
      <td>18</td>
      <td>11/18/1946</td>
      <td>11</td>
      <td>1946</td>
      <td>78</td>
      <td>HLBlack</td>
      <td>78</td>
      <td>HLBlack</td>
    </tr>
    <tr>
      <th>1</th>
      <td>True</td>
      <td>280</td>
      <td>FUNK BROTHERS SEED CO. v. KALO INOCULANT CO.</td>
      <td>92 L. Ed. 2d 588</td>
      <td>1948 U.S. LEXIS 2842</td>
      <td>68 S. Ct. 440</td>
      <td>333 U.S. 127</td>
      <td>7.0</td>
      <td>liberal</td>
      <td>True</td>
      <td>...</td>
      <td>reversed</td>
      <td>True</td>
      <td>16</td>
      <td>2/16/1948</td>
      <td>2</td>
      <td>1948</td>
      <td>87</td>
      <td>FMVinson</td>
      <td>81</td>
      <td>WODouglas</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>85</td>
      <td>YOUNG v. UNITED STATES ex rel. VUITTON ET FILS...</td>
      <td>95 L. Ed. 2d 740</td>
      <td>1987 U.S. LEXIS 2261</td>
      <td>107 S. Ct. 2124</td>
      <td>481 U.S. 787</td>
      <td>3.0</td>
      <td>liberal</td>
      <td>True</td>
      <td>...</td>
      <td>reversed</td>
      <td>True</td>
      <td>26</td>
      <td>5/26/1987</td>
      <td>5</td>
      <td>1987</td>
      <td>92</td>
      <td>WJBrennan</td>
      <td>92</td>
      <td>WJBrennan</td>
    </tr>
    <tr>
      <th>3</th>
      <td>True</td>
      <td>71</td>
      <td>UNITED STATES v. GLAXO GROUP LTD. et al.</td>
      <td>35 L. Ed. 2d 104</td>
      <td>1973 U.S. LEXIS 26</td>
      <td>93 S. Ct. 861</td>
      <td>410 U.S. 52</td>
      <td>7.0</td>
      <td>liberal</td>
      <td>True</td>
      <td>...</td>
      <td>reversed</td>
      <td>True</td>
      <td>22</td>
      <td>1/22/1973</td>
      <td>1</td>
      <td>1973</td>
      <td>99</td>
      <td>WEBurger</td>
      <td>95</td>
      <td>BRWhite</td>
    </tr>
    <tr>
      <th>4</th>
      <td>True</td>
      <td>250</td>
      <td>UNITED STATES v. NEW WRINKLE, INC. ET AL.</td>
      <td>96 L. Ed. 2d 417</td>
      <td>1952 U.S. LEXIS 2811</td>
      <td>72 S. Ct. 350</td>
      <td>342 U.S. 371</td>
      <td>4.0</td>
      <td>liberal</td>
      <td>True</td>
      <td>...</td>
      <td>reversed</td>
      <td>True</td>
      <td>4</td>
      <td>2/4/1952</td>
      <td>2</td>
      <td>1952</td>
      <td>87</td>
      <td>FMVinson</td>
      <td>79</td>
      <td>SFReed</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 56 columns</p>
</div>




```python
crashes_idx.shape
```




    (5, 56)




```python
# Indexing by label
crashes_label = crashes.loc[:5,:]
```


```python
crashes_label.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>3_judge_dc</th>
      <th>docket</th>
      <th>name</th>
      <th>citation.led</th>
      <th>citation.lexis</th>
      <th>citation.sct</th>
      <th>citation.us</th>
      <th>decision.authority</th>
      <th>decision.direction</th>
      <th>decision.dissent agrees</th>
      <th>...</th>
      <th>decision.case.disposition</th>
      <th>decision.case.unusual</th>
      <th>decision.date.day</th>
      <th>decision.date.full</th>
      <th>decision.date.month</th>
      <th>decision.date.year</th>
      <th>voting.majority assigner.id</th>
      <th>voting.majority assigner.name</th>
      <th>voting.majority writer.id</th>
      <th>voting.majority writer.name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>True</td>
      <td>24</td>
      <td>HALLIBURTON OIL WELL CEMENTING CO. v. WALKER e...</td>
      <td>91 L. Ed. 3</td>
      <td>1946 U.S. LEXIS 1724</td>
      <td>67 S. Ct. 6</td>
      <td>329 U.S. 1</td>
      <td>4.0</td>
      <td>liberal</td>
      <td>True</td>
      <td>...</td>
      <td>reversed</td>
      <td>True</td>
      <td>18</td>
      <td>11/18/1946</td>
      <td>11</td>
      <td>1946</td>
      <td>78</td>
      <td>HLBlack</td>
      <td>78</td>
      <td>HLBlack</td>
    </tr>
    <tr>
      <th>1</th>
      <td>True</td>
      <td>280</td>
      <td>FUNK BROTHERS SEED CO. v. KALO INOCULANT CO.</td>
      <td>92 L. Ed. 2d 588</td>
      <td>1948 U.S. LEXIS 2842</td>
      <td>68 S. Ct. 440</td>
      <td>333 U.S. 127</td>
      <td>7.0</td>
      <td>liberal</td>
      <td>True</td>
      <td>...</td>
      <td>reversed</td>
      <td>True</td>
      <td>16</td>
      <td>2/16/1948</td>
      <td>2</td>
      <td>1948</td>
      <td>87</td>
      <td>FMVinson</td>
      <td>81</td>
      <td>WODouglas</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>85</td>
      <td>YOUNG v. UNITED STATES ex rel. VUITTON ET FILS...</td>
      <td>95 L. Ed. 2d 740</td>
      <td>1987 U.S. LEXIS 2261</td>
      <td>107 S. Ct. 2124</td>
      <td>481 U.S. 787</td>
      <td>3.0</td>
      <td>liberal</td>
      <td>True</td>
      <td>...</td>
      <td>reversed</td>
      <td>True</td>
      <td>26</td>
      <td>5/26/1987</td>
      <td>5</td>
      <td>1987</td>
      <td>92</td>
      <td>WJBrennan</td>
      <td>92</td>
      <td>WJBrennan</td>
    </tr>
    <tr>
      <th>3</th>
      <td>True</td>
      <td>71</td>
      <td>UNITED STATES v. GLAXO GROUP LTD. et al.</td>
      <td>35 L. Ed. 2d 104</td>
      <td>1973 U.S. LEXIS 26</td>
      <td>93 S. Ct. 861</td>
      <td>410 U.S. 52</td>
      <td>7.0</td>
      <td>liberal</td>
      <td>True</td>
      <td>...</td>
      <td>reversed</td>
      <td>True</td>
      <td>22</td>
      <td>1/22/1973</td>
      <td>1</td>
      <td>1973</td>
      <td>99</td>
      <td>WEBurger</td>
      <td>95</td>
      <td>BRWhite</td>
    </tr>
    <tr>
      <th>4</th>
      <td>True</td>
      <td>250</td>
      <td>UNITED STATES v. NEW WRINKLE, INC. ET AL.</td>
      <td>96 L. Ed. 2d 417</td>
      <td>1952 U.S. LEXIS 2811</td>
      <td>72 S. Ct. 350</td>
      <td>342 U.S. 371</td>
      <td>4.0</td>
      <td>liberal</td>
      <td>True</td>
      <td>...</td>
      <td>reversed</td>
      <td>True</td>
      <td>4</td>
      <td>2/4/1952</td>
      <td>2</td>
      <td>1952</td>
      <td>87</td>
      <td>FMVinson</td>
      <td>79</td>
      <td>SFReed</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 56 columns</p>
</div>




```python
crashes_label.shape
```




    (6, 56)




```python
crashes_label.index
```




    RangeIndex(start=0, stop=6, step=1)




```python
crashes.loc[:20,["decision.direction", "decision.date.year"]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>decision.direction</th>
      <th>decision.date.year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>liberal</td>
      <td>1946</td>
    </tr>
    <tr>
      <th>1</th>
      <td>liberal</td>
      <td>1948</td>
    </tr>
    <tr>
      <th>2</th>
      <td>liberal</td>
      <td>1987</td>
    </tr>
    <tr>
      <th>3</th>
      <td>liberal</td>
      <td>1973</td>
    </tr>
    <tr>
      <th>4</th>
      <td>liberal</td>
      <td>1952</td>
    </tr>
    <tr>
      <th>5</th>
      <td>liberal</td>
      <td>1976</td>
    </tr>
    <tr>
      <th>6</th>
      <td>liberal</td>
      <td>1947</td>
    </tr>
    <tr>
      <th>7</th>
      <td>liberal</td>
      <td>1964</td>
    </tr>
    <tr>
      <th>8</th>
      <td>liberal</td>
      <td>1984</td>
    </tr>
    <tr>
      <th>9</th>
      <td>liberal</td>
      <td>1964</td>
    </tr>
    <tr>
      <th>10</th>
      <td>liberal</td>
      <td>1961</td>
    </tr>
    <tr>
      <th>11</th>
      <td>liberal</td>
      <td>1969</td>
    </tr>
    <tr>
      <th>12</th>
      <td>liberal</td>
      <td>1950</td>
    </tr>
    <tr>
      <th>13</th>
      <td>liberal</td>
      <td>1964</td>
    </tr>
    <tr>
      <th>14</th>
      <td>liberal</td>
      <td>1948</td>
    </tr>
    <tr>
      <th>15</th>
      <td>liberal</td>
      <td>1964</td>
    </tr>
    <tr>
      <th>16</th>
      <td>liberal</td>
      <td>2008</td>
    </tr>
    <tr>
      <th>17</th>
      <td>liberal</td>
      <td>1972</td>
    </tr>
    <tr>
      <th>18</th>
      <td>liberal</td>
      <td>1978</td>
    </tr>
    <tr>
      <th>19</th>
      <td>liberal</td>
      <td>1966</td>
    </tr>
    <tr>
      <th>20</th>
      <td>liberal</td>
      <td>1965</td>
    </tr>
  </tbody>
</table>
</div>




```python
crashes["decision.direction"].value_counts()
```




    liberal          4456
    conservative     4207
    unspecifiable     140
    Name: decision.direction, dtype: int64




```python
type(crashes["decision.direction"])
```




    pandas.core.series.Series




```python
frame = pd.DataFrame(
    [
    [1,2],
    ["Boris Yeltsin", "Mikhail Gorbachev"]
    ],
    index=["row1", "row2"],
    columns=["column1", "column2"]
)
frame
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>column1</th>
      <th>column2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>row1</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>row2</th>
      <td>Boris Yeltsin</td>
      <td>Mikhail Gorbachev</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Input In [1], in <module>
    ----> 1 jt -t
    

    NameError: name 'jt' is not defined

