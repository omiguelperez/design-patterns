'use strict';

function Pizza () {
  this.masa = null;
  this.salsa = null;
  this.relleno = null;
};

Pizza.prototype.doSomething = function () {
  console.log(`${this.masa} - ${this.salsa} - ${this.relleno}`);
};

module.exports = Pizza;
