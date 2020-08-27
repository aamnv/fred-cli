# FRED CLI

TL;DR: CLI app to interface with the FRED (Federal Reserve Economic Data) API.

[![fred-cli demo](https://asciinema.org/a/356315.svg)](https://asciinema.org/a/356315)

> Fancy video thanks to: [asciinema](https://asciinema.org/)

## Table of Contents

- [Requirements](#Requirements)
- [Installation](#Installation)
- [Documentation](#Documentation)
    - [Search](#Search)
    - [About](#About)
    - [Get](#Get)
- [License](#License)

## Requirements

- Python 3.6+
- Package Dependencies:
    - [tabulate](https://github.com/astanin/python-tabulate)
    - [fred](https://github.com/zachwill/fred)
    - [click](https://github.com/pallets/click/)

## Installation

Assuming you have Python 3.6+ installed, you can install fred-cli via pip:

`pip install fred-cli`

You'll also need an API key for FRED, which you can get for free via [the FRED website](https://research.stlouisfed.org/docs/api/api_key.html). Once you have your API key, export an environment variable that `fred-cli` can use:

`export FRED_API_KEY=yourkeyhere`

## Documentation

`fred-cli` supports three main methods in `v1`:

- search
- about
- get

### Search

There are **~766,000** unique economic time series available via [FRED](). Luckily, `fred-cli` makes it easy to search through this massive list using search.

**Example**:

`fred search gross national product`

**Returns**:

| ID               | Title                               | Units                        | Freq.   |
|------------------|-------------------------------------|------------------------------|---------|
| GNP              | Gross National Product              | Bil. of $                    | Q       |
| GNPA             | Gross National Product              | Bil. of $                    | A       |
| A001RP1Q027SBEA  | Gross National Product              | % Chg. from Preceding Period | Q       |
| A001RP1A027NBEA  | Gross National Product              | % Chg. from Preceding Period | A       |
| MKTGNIUSA646NWDB | Gross National Income for United St | Current $                    | A       |
| GNPC96           | Real Gross National Product         | Bil. of Chn. 2012 $          | Q       |
| A001RO1Q156NBEA  | Real Gross National Product         | % Chg. from Qtr.  1 Yr. Ago  | Q       |
| GNPCA            | Real Gross National Product         | Bil. of Chn. 2012 $          | A       |
| A001RL1A225NBEA  | Real Gross National Product         | % Chg. from Preceding Period | A       |
| A001RL1Q225SBEA  | Real Gross National Product         | % Chg. from Preceding Period | Q       |
| GNPDEF           | Gross National Product: Implicit Pr | Index 2012=100               | Q       |
| A001RI1Q225SBEA  | Gross National Product: Implicit Pr | % Chg. from Preceding Period | Q       |
| A001RI1A225NBEA  | Gross National Product: Implicit Pr | % Chg. from Preceding Period | A       |
| MKTGNIPHA646NWDB | Gross National Income for Philippin | Current $                    | A       |

> Page: 1 / 34 | next page (n), prev page (b), exit (e)

Search provides 15 results per page and pagination using user keyboard input:

- n = next page
- b = previous page
- e = to exit and issue new commands

### About

The search function only provides summary information on retrieved metrics and should be thought of as an entry point. That's why `fred-cli` also provides an `about` method that fetches more detailed information on a specific metric - given its ID.

**Example**:

`fred about GNP`

**Returns**:

| Series Info:         |                                 |
|----------------------|---------------------------------|
| ID:                  | GNP                             |
| Title:               | Gross National Product          |
| Obs. Start:          | 1947-01-01                      |
| Obs. End:            | 2020-04-01                      |
| Frequency:           | Quarterly                       |
| Units:               | Billions of Dollars             |
| Seasonal Adjustment: | Seasonally Adjusted Annual Rate |
| Last Updated:        | 2020-08-27 08:00:33-05          |

Using the `search` and `about` method in tandem will allow users to properly discover and learn about available metrics.

### Get

Finally, there's the workhorse of the CLI - the `get` method. This method fetches an the time series for a user specified metric -  given a metric ID. Metric IDs can be found using the `search` method [described above](#Search).

**Example**:

`fred get GNP`

**Returns**:

| Period     |     GNP |
|------------|---------|
| 2015-07-01 | 18560.9 |
| 2015-10-01 | 18611.9 |
| 2016-01-01 | 18684.3 |
| 2016-04-01 | 18874.5 |
| 2016-07-01 | 19043.7 |
| 2016-10-01 | 19306   |
| 2017-01-01 | 19514.1 |
| 2017-04-01 | 19646.8 |
| 2017-07-01 | 19918.7 |
| 2017-10-01 | 20261.5 |
| 2018-01-01 | 20556.8 |
| 2018-04-01 | 20844.2 |
| 2018-07-01 | 21002.7 |
| 2018-10-01 | 21182.6 |
| 2019-01-01 | 21361.8 |
| 2019-04-01 | 21601   |
| 2019-07-01 | 21820.1 |
| 2019-10-01 | 22028.5 |
| 2020-01-01 | 21804.3 |
| 2020-04-01 | 19616.8 |

`get` defaults to fetching five years worth of data - but users can specify a year period via the `-y` argument:

**Example**:

`fred get -y 1 GNP`

**Returns**:

| Period     |     GNP |
|------------|---------|
| 2019-07-01 | 21820.1 |
| 2019-10-01 | 22028.5 |
| 2020-01-01 | 21804.3 |
| 2020-04-01 | 19616.8 |

## License

MIT License

Copyright (c) 2020 Aadhi Manivannan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.