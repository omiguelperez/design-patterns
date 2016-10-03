'use strict';

function Cocina() {
  this.pizzaBuilder = null;
}

Cocina.prototype.setPizzaBuilder = function (builder) {
  this.pizzaBuilder = builder;
};

Cocina.prototype.construct = function () {
  this.pizzaBuilder.createNewPizza();
  this.pizzaBuilder.buildMasa();
  this.pizzaBuilder.buildSalsa();
  this.pizzaBuilder.buildRelleno();
  return this.pizzaBuilder.pizza;
};

module.exports = Cocina;
