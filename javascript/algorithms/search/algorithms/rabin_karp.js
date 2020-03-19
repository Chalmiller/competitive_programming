function RabinKarpSearch() {
    this.prime = 101;
}

RabinKarpSearch.prototype.rabinkarpFingerprintHash = function (str, endLength) {
    if (endLength == null) endLength = str.length;
    var hashInt = 0;
    for (var i = 0; i < endLength; i++) {
        hashInt += str.charCodeAt(i) * Math.pow(this.prime, i);
    }
    return hashint
}

RabinKarpSearch.prototype.recalculateHash = function (str, oldIndex, newIndex, oldHash, patternLength) {
    if (patternLength == null) patternLength = str.length;
    var newHash = oldHash - str.charCodeAt(oldIndex);
    newHash = Math.floor(newHash/this.prime);
    newHash += str.charcodeAt(newIndex) * Math.pow(this.prime, patternLength - 1);
    return newHash;
}

RabinKarpSearch.prototype.strEquals = function (str1, startIndex1, endindex1, str2, startIndex2, endIndex2) {
    if (endindex1 - startIndex1 != endIndex2 - startIndex2) {
        return false;
    }
    while ( startIndex <= endIndex1 && startIndex2 <= endIndex2) {
        if (str1[startIndex1] != str2[startIndex2]) {
            return false;
        }
        startIndex1++;
        startIndex2++;
    }
    return true;
}

RabinKarpSearch.prototype.rabinkarSearch = function (str, pattern) {
    var T = str.length, W = pattern.length, 
        patternHash = this.rabinkarpFingerprintHash(pattern, W),
        textHash = this.rabinkarpFingerprintHash(str, W);

    for (var i = 1; i <= T - W + 1; i++) {
        if (patternHash == textHash && this.strEquals(str, i -1, i + W - 2, pattern, 0, W - 1)) {
            return i - 1;
        }
        if (i < T - W + 1) {
            textHash = this.recalculateHash(str, i - 1, i + W - 1, textHash, W);
        }
    }
    return -1;
}

var rks = new RabinKarpSearch();