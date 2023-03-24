odoo.define('product_grade.receipt', function (require) {
"use strict";
   var { Orderline } = require('point_of_sale.models');
   var Registries = require('point_of_sale.Registries');
   const CustomOrder = (Orderline) => class CustomOrder extends Orderline {
       export_for_printing() {
           var result = super.export_for_printing(...arguments);
           result.grade = this.product.grade
           console.log(result)
           console.log('this',this)
           return result;
   }
   }
       Registries.Model.extend(Orderline, CustomOrder);
   });