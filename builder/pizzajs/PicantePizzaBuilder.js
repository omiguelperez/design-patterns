'use strict';

const Pizza = require('./Pizza');
const PizzaBuilder = require('./PizzaBuilder');

function PicantePizzaBuilder() {
  this.pizza = null;
}

PicantePizzaBuilder.prototype.createNewPizza = function () {
  this.pizza = new Pizza();
};

PicantePizzaBuilder.prototype.buildMasa = function () {
  this.pizza.masa = 'cocida';
};

PicantePizzaBuilder.prototype.buildSalsa = function () {
  this.pizza.salsa = 'picante';
};

PicantePizzaBuilder.prototype.buildRelleno = function () {
  this.pizza.relleno = 'pimienta+salchichon';
};

PicantePizzaBuilder.prototype.getPizza = function () {
  return this.pizza;
};

module.exports = PicantePizzaBuilder;
