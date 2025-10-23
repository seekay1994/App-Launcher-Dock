import json
import shutil
import os
import sys

PROPERTIES_TO_ADD = {
      "appdockalpha" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true",
      "fraction" : True,
      "index" : 607,
      "max" : 1,
      "min" : 0,
      "order" : 707,
      "precision" : 3,
      "step" : 0.01,
      "text" : "‎ ‎ ‎ ‎ <small>Opacity</small>",
      "type" : "slider",
      "value" : 0.35
  },
  "appdockapplyusertexture1" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable1.value == true",
      "index" : 623,
      "order" : 723,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockapplyusertexture10" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable10.value == true",
      "index" : 659,
      "order" : 759,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockapplyusertexture11" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable11.value == true",
      "index" : 663,
      "order" : 763,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockapplyusertexture12" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable12.value == true",
      "index" : 667,
      "order" : 767,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockapplyusertexture13" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable13.value == true",
      "index" : 671,
      "order" : 771,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockapplyusertexture14" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable14.value == true",
      "index" : 675,
      "order" : 775,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockapplyusertexture15" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable15.value == true",
      "index" : 679,
      "order" : 779,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockapplyusertexture16" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable16.value == true",
      "index" : 683,
      "order" : 783,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockapplyusertexture17" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable17.value == true",
      "index" : 687,
      "order" : 787,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockapplyusertexture18" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable18.value == true",
      "index" : 691,
      "order" : 791,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockapplyusertexture19" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable19.value == true",
      "index" : 695,
      "order" : 795,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockapplyusertexture2" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable2.value == true",
      "index" : 627,
      "order" : 727,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockapplyusertexture20" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable20.value == true",
      "index" : 699,
      "order" : 799,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockapplyusertexture21" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable21.value == true",
      "index" : 703,
      "order" : 803,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockapplyusertexture22" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable22.value == true",
      "index" : 707,
      "order" : 807,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockapplyusertexture23" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable23.value == true",
      "index" : 711,
      "order" : 811,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockapplyusertexture24" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable24.value == true",
      "index" : 715,
      "order" : 815,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockapplyusertexture3" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable3.value == true",
      "index" : 631,
      "order" : 731,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockapplyusertexture4" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable4.value == true",
      "index" : 635,
      "order" : 735,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockapplyusertexture5" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable5.value == true",
      "index" : 639,
      "order" : 739,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockapplyusertexture6" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable6.value == true",
      "index" : 643,
      "order" : 743,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockapplyusertexture7" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable7.value == true",
      "index" : 647,
      "order" : 747,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockapplyusertexture8" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable8.value == true",
      "index" : 651,
      "order" : 751,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockapplyusertexture9" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable9.value == true",
      "index" : 655,
      "order" : 755,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>Use Custom Icon</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockautohide" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true",
      "index" : 609,
      "order" : 709,
      "text" : "‎ ‎ ‎ ‎ <small>Auto Hide</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockcolor" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true",
      "index" : 606,
      "order" : 706,
      "text" : "‎ ‎ ‎ ‎ <small>Color</small>",
      "type" : "color",
      "value" : "0 0 0"
  },
  "appdockedgethreshold" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && draganddropdock.value == true",
      "fraction" : False,
      "index" : 604,
      "max" : 15,
      "min" : -15,
      "order" : 704,
      "text" : "‎ ‎ ‎ ‎ <small>Edge Threshold</small>",
      "type" : "slider",
      "value" : 10
  },
  "appdockenable1" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 621,
      "order" : 721,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #1</small>",
      "type" : "bool",
      "value" : True
  },
  "appdockenable10" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 657,
      "order" : 757,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #10</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockenable11" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 661,
      "order" : 761,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #11</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockenable12" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 665,
      "order" : 765,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #12</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockenable13" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 669,
      "order" : 769,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #13</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockenable14" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 673,
      "order" : 773,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #14</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockenable15" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 677,
      "order" : 777,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #15</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockenable16" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 681,
      "order" : 781,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #16</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockenable17" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 685,
      "order" : 785,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #17</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockenable18" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 689,
      "order" : 789,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #18</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockenable19" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 693,
      "order" : 793,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #19</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockenable2" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 625,
      "order" : 725,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #2</small>",
      "type" : "bool",
      "value" : True
  },
  "appdockenable20" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 697,
      "order" : 797,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #20</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockenable21" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 701,
      "order" : 801,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #21</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockenable22" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 705,
      "order" : 805,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #22</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockenable23" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 709,
      "order" : 809,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #23</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockenable24" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 713,
      "order" : 813,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #24</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockenable3" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 629,
      "order" : 729,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #3</small>",
      "type" : "bool",
      "value" : True
  },
  "appdockenable4" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 633,
      "order" : 733,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #4</small>",
      "type" : "bool",
      "value" : True
  },
  "appdockenable5" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 637,
      "order" : 737,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #5</small>",
      "type" : "bool",
      "value" : True
  },
  "appdockenable6" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 641,
      "order" : 741,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #6</small>",
      "type" : "bool",
      "value" : True
  },
  "appdockenable7" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 645,
      "order" : 745,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #7</small>",
      "type" : "bool",
      "value" : True
  },
  "appdockenable8" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 649,
      "order" : 749,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #8</small>",
      "type" : "bool",
      "value" : True
  },
  "appdockenable9" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 653,
      "order" : 753,
      "text" : "‎ ‎ ‎ ‎ <small>Enable #9</small>",
      "type" : "bool",
      "value" : False
  },
  "appdockenabled" : 
  {
      "condition" : "appdocksettings.value == true",
      "index" : 602,
      "order" : 702,
      "text" : "‎ ‎ ‎ ‎ Enabled",
      "type" : "bool",
      "value" : True
  },
  "appdockframespacing" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true",
      "fraction" : True,
      "index" : 617,
      "max" : 1,
      "min" : 0,
      "order" : 717,
      "precision" : 3,
      "step" : 0.01,
      "text" : "‎ ‎ ‎ ‎ <small>Frame Spacing</small>",
      "type" : "slider",
      "value" : 0.2
  },
  "appdocknotchsize" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true",
      "fraction" : True,
      "index" : 618,
      "max" : 1,
      "min" : 0,
      "order" : 718,
      "precision" : 3,
      "step" : 0.01,
      "text" : "‎ ‎ ‎ ‎ <small>Rounding</small>",
      "type" : "slider",
      "value" : 0.5
  },
  "appdockradius" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true",
      "fraction" : True,
      "index" : 614,
      "max" : 1,
      "min" : 0,
      "order" : 714,
      "precision" : 3,
      "step" : 0.01,
      "text" : "‎ ‎ ‎ ‎ <small>Cursor Radius</small>",
      "type" : "slider",
      "value" : 0.2
  },
  "appdockscale" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true",
      "fraction" : True,
      "index" : 612,
      "max" : 1.5,
      "min" : 0.3,
      "order" : 712,
      "precision" : 3,
      "step" : 0.01,
      "text" : "‎ ‎ ‎ ‎ <small>Scale</small>",
      "type" : "slider",
      "value" : 0.8
  },
  "appdockscalemultiplier" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true",
      "fraction" : True,
      "index" : 613,
      "max" : 5,
      "min" : 1,
      "order" : 713,
      "precision" : 2,
      "step" : 0.1,
      "text" : "‎ ‎ ‎ ‎ <small>Hover Scale</small>",
      "type" : "slider",
      "value" : 2
  },
  "appdocksettings" : 
  {
      "index" : 601,
      "order" : 701,
      "text" : "<b>App Dock Settings</b>",
      "type" : "bool",
      "value" : False
  },
  "appdocksetup" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true",
      "index" : 620,
      "order" : 720,
      "text" : "‎ ‎ ‎ ‎  Shortcut Setup",
      "type" : "bool",
      "value" : False
  },
  "appdockspacing" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true",
      "fraction" : True,
      "index" : 616,
      "max" : 1,
      "min" : 0,
      "order" : 716,
      "precision" : 3,
      "step" : 0.01,
      "text" : "‎ ‎ ‎ ‎ <small>Icon Spacing</small>",
      "type" : "slider",
      "value" : 0.3
  },
  "draganddropdock" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true",
      "index" : 603,
      "order" : 703,
      "text" : "‎ ‎ ‎ ‎ <small>Drag and Drop</small>",
      "type" : "bool",
      "value" : False
  },
  "launcher1" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable1.value == true",
      "index" : 622,
      "order" : 722,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#1</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "launcher10" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable10.value == true",
      "index" : 658,
      "order" : 758,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#10</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "launcher11" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable11.value == true",
      "index" : 662,
      "order" : 762,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#11</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "launcher12" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable12.value == true",
      "index" : 666,
      "order" : 766,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#12</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "launcher13" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable13.value == true",
      "index" : 670,
      "order" : 770,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#13</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "launcher14" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable14.value == true",
      "index" : 674,
      "order" : 774,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#14</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "launcher15" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable15.value == true",
      "index" : 678,
      "order" : 778,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#15</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "launcher16" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable16.value == true",
      "index" : 682,
      "order" : 782,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#16</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "launcher17" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable17.value == true",
      "index" : 686,
      "order" : 786,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#17</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "launcher18" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable18.value == true",
      "index" : 690,
      "order" : 790,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#18</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "launcher19" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable19.value == true",
      "index" : 694,
      "order" : 794,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#19</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "launcher2" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable2.value == true",
      "index" : 626,
      "order" : 726,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#2</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "launcher20" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable20.value == true",
      "index" : 698,
      "order" : 798,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#20</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "launcher21" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable21.value == true",
      "index" : 702,
      "order" : 802,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#21</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "launcher22" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable22.value == true",
      "index" : 706,
      "order" : 806,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#22</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "launcher23" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable23.value == true",
      "index" : 710,
      "order" : 810,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#23</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "launcher24" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable24.value == true",
      "index" : 714,
      "order" : 814,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#24</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "launcher3" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable3.value == true",
      "index" : 630,
      "order" : 730,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#3</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "launcher4" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable4.value == true",
      "index" : 634,
      "order" : 734,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#4</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "launcher5" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable5.value == true",
      "index" : 638,
      "order" : 738,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#5</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "launcher6" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable6.value == true",
      "index" : 642,
      "order" : 742,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#6</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "launcher7" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable7.value == true",
      "index" : 646,
      "order" : 746,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#7</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "launcher8" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable8.value == true",
      "index" : 650,
      "order" : 750,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#8</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "launcher9" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable9.value == true",
      "index" : 654,
      "order" : 754,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small>#9</small>",
      "type" : "usershortcut",
      "value" : ""
  },
  "texttitle25656" : 
  {
      "condition" : "appdocksettings.value == true",
      "index" : 605,
      "order" : 705,
      "text" : "",
      "type" : "text"
  },
  "texttitle35656" : 
  {
      "condition" : "appdocksettings.value == true",
      "index" : 600,
      "order" : 700,
      "text" : "",
      "type" : "text"
  },
  "texttitle45656" : 
  {
      "condition" : "appdocksettings.value == true",
      "index" : 611,
      "order" : 711,
      "text" : "",
      "type" : "text"
  },
  "texttitle5656" : 
  {
      "condition" : "appdocksettings.value == true",
      "index" : 608,
      "order" : 708,
      "text" : "",
      "type" : "text"
  },
  "texttitle56586" : 
  {
      "condition" : "appdocksettings.value == true",
      "index" : 615,
      "order" : 715,
      "text" : "",
      "type" : "text"
  },
  "texttitle6" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true",
      "index" : 619,
      "order" : 719,
      "text" : "",
      "type" : "text"
  },
  "texttitled2" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdockautohide.value == true",
      "index" : 610,
      "order" : 710,
      "text" : "<h6>The dock will remain visible as long as \"App Dock Settings\" are opened</h6>",
      "type" : "text"
  },
  "usertexture1" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable1.value == true && appdockapplyusertexture1.value == true",
      "index" : 624,
      "order" : 724,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  },
  "usertexture10" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable10.value == true && appdockapplyusertexture10.value == true",
      "index" : 660,
      "order" : 760,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  },
  "usertexture11" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable11.value == true && appdockapplyusertexture11.value == true",
      "index" : 664,
      "order" : 764,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  },
  "usertexture12" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable12.value == true && appdockapplyusertexture12.value == true",
      "index" : 668,
      "order" : 768,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  },
  "usertexture13" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable13.value == true && appdockapplyusertexture13.value == true",
      "index" : 672,
      "order" : 772,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  },
  "usertexture14" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable14.value == true && appdockapplyusertexture14.value == true",
      "index" : 676,
      "order" : 776,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  },
  "usertexture15" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable15.value == true && appdockapplyusertexture15.value == true",
      "index" : 680,
      "order" : 780,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  },
  "usertexture16" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable16.value == true && appdockapplyusertexture16.value == true",
      "index" : 684,
      "order" : 784,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  },
  "usertexture17" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable17.value == true && appdockapplyusertexture17.value == true",
      "index" : 688,
      "order" : 788,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  },
  "usertexture18" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable18.value == true && appdockapplyusertexture18.value == true",
      "index" : 692,
      "order" : 792,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  },
  "usertexture19" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable19.value == true && appdockapplyusertexture19.value == true",
      "index" : 696,
      "order" : 796,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  },
  "usertexture2" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable2.value == true && appdockapplyusertexture2.value == true",
      "index" : 628,
      "order" : 728,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  },
  "usertexture20" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable20.value == true && appdockapplyusertexture20.value == true",
      "index" : 700,
      "order" : 800,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  },
  "usertexture21" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable21.value == true && appdockapplyusertexture21.value == true",
      "index" : 704,
      "order" : 804,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  },
  "usertexture22" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable22.value == true && appdockapplyusertexture22.value == true",
      "index" : 708,
      "order" : 808,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  },
  "usertexture23" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable23.value == true && appdockapplyusertexture23.value == true",
      "index" : 712,
      "order" : 812,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  },
  "usertexture24" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable24.value == true && appdockapplyusertexture24.value == true",
      "index" : 716,
      "order" : 816,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  },
  "usertexture3" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable3.value == true && appdockapplyusertexture3.value == true",
      "index" : 632,
      "order" : 732,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  },
  "usertexture4" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable4.value == true && appdockapplyusertexture4.value == true",
      "index" : 636,
      "order" : 736,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  },
  "usertexture5" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable5.value == true && appdockapplyusertexture5.value == true",
      "index" : 640,
      "order" : 740,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  },
  "usertexture6" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable6.value == true && appdockapplyusertexture6.value == true",
      "index" : 644,
      "order" : 744,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  },
  "usertexture7" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable7.value == true && appdockapplyusertexture7.value == true",
      "index" : 648,
      "order" : 748,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  },
  "usertexture8" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable8.value == true && appdockapplyusertexture8.value == true",
      "index" : 652,
      "order" : 752,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  },
  "usertexture9" : 
  {
      "condition" : "appdocksettings.value == true && appdockenabled.value == true && appdocksetup.value == true && appdockenable9.value == true && appdockapplyusertexture9.value == true",
      "index" : 656,
      "order" : 756,
      "text" : "‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ <small></small>",
      "type" : "scenetexture",
      "value" : ""
  }
}

def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and PyInstaller."""
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def validate_project_folder():
    """Ensure script is executed in a valid project folder."""
    has_project = os.path.isfile("project.json")
    has_materials = os.path.isdir("materials")
    if not (has_project and has_materials):
        print("This needs to be executed in a project folder")
        return False
    return True

def create_backup(project_file):
    """Create a backup of the project.json file."""
    backup_file = os.path.splitext(project_file)[0] + "_BACKUP.json"
    shutil.copy2(project_file, backup_file)
    print(f"Backup created successfully: {backup_file}")
    return backup_file

def merge_properties(project_file='project.json'):
    """Merge additional properties into project.json (without creating new structures)."""
    with open(project_file, 'r', encoding='utf-8') as f:
        project_data = json.load(f)

    if "general" not in project_data or "properties" not in project_data["general"]:
        print("project.json does not contain a valid 'general' -> 'properties' structure")
        return

    project_data["general"]["properties"].update(PROPERTIES_TO_ADD)

    with open(project_file, 'w', encoding='utf-8') as f:
        json.dump(project_data, f, indent='\t', ensure_ascii=False)

    print(f"Properties merged into {project_file}")

def copy_textures(materials_folder='materials'):
    """Copy all texture files from the embedded 'textures' folder into 'materials'."""
    textures_folder = get_resource_path('textures')

    texture_files = [
        f for f in os.listdir(textures_folder)
        if os.path.isfile(os.path.join(textures_folder, f))
    ]

    for filename in texture_files:
        source = os.path.join(textures_folder, filename)
        destination = os.path.join(materials_folder, filename)
        try:
            shutil.copy2(source, destination)
        except Exception as e:
            print(f"Failed to copy {filename}: {e}")

    print("All textures copied successfully")

if __name__ == "__main__":
    print("App Launcher Dock - Easy Setup")
    print("=" * 50)

    if not validate_project_folder():
        input("\nPress Enter to close...")
        sys.exit(1)

    try:
        create_backup("project.json")
        merge_properties("project.json")
        copy_textures("materials")
    except Exception as e:
        print(f"\nError occurred: {e}")
        import traceback
        traceback.print_exc()

    print("=" * 50)
    input("Press Enter to close...")
