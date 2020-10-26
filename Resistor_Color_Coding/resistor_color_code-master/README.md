<style>
    table, td {
	border: 1px solid black;
	border-collapse: collapse;
	padding: 5px;
    }
    th {
	border: 1px solid black;
	border-collapse: collapse;
	padding: 5px;
	background-color: #eeeeee;
    }
    pre {
	background-color:#DDDDDD;
	border-color:#BBBBBB;
	border-width:2px;
	border-style:solid;
	padding:4px;
    }
</style>

**_Note:_** Because I'm running my own servers for serveral years, main development is done at at https://git.ypbind.de/cgit/resistor_color_code/

----

Decode resistor color bands
===============================================

## Preface

The purpose of this tool is to decode the color bands found on resistors.

Color codes of resistors come in two "flavors": 4-band and 5-band. Both types are coded
by a number of colored bands around the resistor encodiing the resistance and the tolerance:

![Schematic of color bands on 4-band resistor](/images/4_bands.png "Schematic of color bands on 4-band resistor")

![Schematic of color bands on 5-band resistor](/images/5_bands.png "Schematic of color bands on 5-band resistor")

<u>*Legend:*</u>

* **D** - digit
* **M** - multiplier
* **T** - tolerance

<table>
    <tr>
	<th><b>Color</b></th>
	<th><b>Value if digit</b></th>
	<th><b>Value if multiplier</b></th>
	<th><b>Value if tolerance</b></th>
	<th><b>Note</b></th>
    <tr>
    <tr>
	<td>black</td>
	<td>0</td>
	<td>1 (=10<sup>0</sup>)</td>
	<td><i>not allowed for tolerance</i></td>
	<td></td>
    <tr>
    <tr>
	<td>brown</td>
	<td>1</td>
	<td>10 (=10<sup>1</sup>)</td>
	<td>1%</td>
	<td><b>(*)</b></td>
    </tr>
    <tr>
	<td>red</td>
	<td>2</td>
	<td>100 (=10<sup>2</sup>)</td>
	<td>2%</td>
	<td><b>(*)</b></td>
    </tr>
    <tr>
	<td>orange</td>
	<td>3</td>
	<td>1000 (=10<sup>3</sup>)</td>
	<td><i>not allowed for tolerance</i></td>
	<td></td>
    </tr>
    <tr>
	<td>yellow</td>
	<td>4</td>
	<td>10000 (=10<sup>4</sup>)</td>
	<td><i>not allowed for tolerance</i></td>
	<td></td>
    </tr>
    <tr>
	<td>green</td>
	<td>5</td>
	<td>100000 (=10<sup>5</sup>)</td>
	<td>0.5%</td>
	<td><b>(*)</b></td>
    </tr>
    <tr>
	<td>blue</td>
	<td>6</td>
	<td>1000000 (=10<sup>6</sup>)</td>
	<td>0.25%</td>
	<td><b>(*)</b></td>
    </tr>
    <tr>
	<td>violet</td>
	<td>7</td>
	<td>10000000 (=10<sup>7</sup>)</td>
	<td>0.1%</td>
	<td><b>(*)</b></td>
    </tr>
    <tr>
	<td>grey</td>
	<td>8</td>
	<td>100000000 (=10<sup>8</sup>)</td>
	<td><i>not allowed for tolerance</i></td>
	<td></td>
    </tr>
    <tr>
	<td>white</td>
	<td>9</td>
	<td>1000000000 (=10<sup>9</sup>)</td>
	<td><i>not allowed for tolerance</i></td>
	<td></td>
    </tr>
    <tr>
	<td>gold</td>
	<td><i>not allowed for digit</i></td>
	<td>0.1 (=10<sup>-1</sup>)</td>
	<td>5%</td>
	<td></td>
    </tr>
    <tr>
	<td>silver</td>
	<td><i>not allowed for digit</i></td>
	<td>0.01 (=10<sup>-2</sup>)</td>
	<td>10%</td>
	<td></td>
    </tr>
    <tr>
	<td>none</td>
	<td><i>not allowed for digit</i></td>
	<td></i>not allows for multiplier</i></td>
	<td>20%</td>
	<td><b>(**)</b></td>
    </tr>

</table>

__(*__) - Only valid as tolerance band if used on a 5-band resistor

__(**)__ - Only valid as ("blank") tolerance band if used on a 4-band resistor

---

## Requirements

Required packages:

  * Python 2.6 or newer

---

## Command line parameters

Supported command line parameters are:

  * `-h` or `--help` - shows a brief help

The color names (see table above) should be given as parameter, separated by comma, output is the resistor value and the tolerance.

Multiple resistor bands can be given (separated by white space), e.g.:

<pre>
resistor_color_code yellow,violet,orange,gold brown,black,orange orange,orange,black,brown,violet
47000.00 +- 5.00%
10000.00 +- 20.00%
3300.00 +- 0.10%
</pre>


---

## License
This program is licenses under [GLPv3](http://www.gnu.org/copyleft/gpl.html).

