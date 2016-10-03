'use strict';

function testBuilderPattern() {
  let shop = new Director();
  let carBuilder = new CarBuilder();
  let car = shop.construct(carBuilder);

  car.doSomethig();
}

function Director() {
  this.carBuilder = null;
}

Director.prototype.construct = function (builder) {
  builder.step1();
  builder.step2();
  return builder.getResult();
};

function Builder() {
  this.step1 = null;
  this.step2 = null;
  this.getResult = null;
}

function CarBuilder() {
  this.car = null;
}

CarBuilder.prototype = Builder;

CarBuilder.prototype.step1 = function () {
  this.car = new Car();
};

CarBuilder.prototype.step2 = function () {
  this.car.addParts();
};

CarBuilder.prototype.getResult = function () {
  return this.car;
};

function Car() {
  this.doors = 0;
}

Car.prototype.addParts = function () {
  this.doors = 4;
};

Car.prototype.doSomethig = function () {
  console.log(`Tengo ${this.doors} puertas.`);
};

testBuilderPattern();
