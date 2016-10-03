'use strict';

const Pizza = require('./Pizza');
const PizzaBuilder = require('./PizzaBuilder');

function HawaiPizzaBuilder() {
  this.pizza = null;
}

HawaiPizzaBuilder.prototype.createNewPizza = function () {
  this.pizza = new Pizza();
};

HawaiPizzaBuilder.prototype.buildMasa = function () {
  this.pizza.masa = 'suave';
};

HawaiPizzaBuilder.prototype.buildSalsa = function () {
  this.pizza.salsa = 'dulce';
};

HawaiPizzaBuilder.prototype.buildRelleno = function () {
  this.pizza.relleno = 'chorizo+alcachofa';
};

HawaiPizzaBuilder.prototype.getPizza = function () {
  return this.pizza;
};

module.exports = HawaiPizzaBuilder;
