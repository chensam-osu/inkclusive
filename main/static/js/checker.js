(function (win,doc) {
    'use strict';
      var entries = doc.querySelectorAll('.results--body'),
      i;

      var exp1 = /\\n/gim;
      var exp2 =/\*([\w ]+)\*/gim;

    
    if ( entries.length > 0 ) {
      for (i = 0; i < entries.length; i = i + 1) {
        entries[i].innerHTML = entries[i].innerHTML.replace(exp1,'<br/><br/>');

        entries[i].innerHTML = entries[i].innerHTML.replace(exp2, '<span class="profanity"><a href="/description/?word=$1">$1</a></span>');
      }
    }
    
  }(this, this.document));
