export default class HolbertonCourse {
    constructor(name, length, students) {
      this.name = name;
      this.length = length;
      this.students = students;
    }
  
    isString(value) {
      if (typeof value !== 'string') throw new TypeError('Expected a string');
    }
  
    isNumber(value) {
      if (typeof value !== 'number') throw new TypeError('Expected a number');
    }
  
    isArrayofStrings(array) {
      if (!Array.isArray(array) || array.some(el => typeof el !== 'string')) {
        throw new TypeError('Expected an array of strings');
      }
    }
  
    get name() {
      return this._name;
    }
  
    set name(value) {
      this.isString(value);
      this._name = value;
    }
  
    get length() {
      return this._length;
    }
  
    set length(value) {
      this.isNumber(value);
      this._length = value;
    }
  
    get students() {
      return this._students;
    }
  
    set students(value) {
      this.isArrayofStrings(value);
      this._students = value;
    }
  }