import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {WINEREVIEW_MODULE_DECLARATIONS, WineReviewRoutingModule} from  './WineReview-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    WineReviewRoutingModule
  ],
  declarations: WINEREVIEW_MODULE_DECLARATIONS,
  exports: WINEREVIEW_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class WineReviewModule { }