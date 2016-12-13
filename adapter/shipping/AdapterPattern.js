'use strict';

function AdapteeShipping() {
  this.request = function (origen, destino, peso) {
    this.origen = origen;
    this.destino = destino;
    this.peso = peso;
    this.total = this.peso * 100;
    console.log(`Desde ${this.origen} hasta ${this.destino}`);
    return this.total;
  };
}

function TargetShipping() {
  this.login = function (credentials) {
    console.log('Iniciando sesión!');
  };

  this.setOrigen = function (origen) {
    this.origen = origen;
  };

  this.setDestino = function (destino) {
    this.destino = destino;
  };

  this.calculate = function (peso) {
    this.peso = peso;
    this.total = this.peso * 100;
    console.log(`Desde ${this.origen} hasta ${this.destino}`);
    return this.total;
  };
}

function ShippingAdapter(credentials) {
  let targetShipping = new TargetShipping();

  targetShipping.login(credentials);

  return {
    request: function (origen, destino, peso) {
      targetShipping.setOrigen(origen);
      targetShipping.setDestino(destino);
      return targetShipping.calculate(peso);
    }
  };
}

function Client() {
  this.run = function () {
    let origen = '153.34.23.244';
    let destino = '235.23.210.34';
    let peso = 23;

    let adaptee = new AdapteeShipping();
    let adapteeTotal = adaptee.request(origen, destino, peso);
    console.log('adapteeTotal', adapteeTotal);

    let credentials = 'user/pass';
    let adapter = new ShippingAdapter(credentials);
    let adapterTotal = adapter.request(origen, destino, peso);
    console.log('adapterTotal', adapterTotal);
  };
}

let client = new Client();
client.run();
