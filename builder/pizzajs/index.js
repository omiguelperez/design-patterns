'use strict';

const Cocina = require('./Cocina');
const PicantePizzaBuilder = require('./PicantePizzaBuilder');
const HawaiPizzaBuilder = require('./HawaiPizzaBuilder');

let cocina1 = new Cocina();
let cocina2 = new Cocina();

let picantePizzaBuilder = new PicantePizzaBuilder();
let hawaiPizzaBuilder = new HawaiPizzaBuilder();

cocina1.setPizzaBuilder(picantePizzaBuilder);
console.log(cocina1.construct());

cocina2.setPizzaBuilder(hawaiPizzaBuilder);
console.log(cocina2.construct());
