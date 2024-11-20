import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Wine-card.component.html',
  styleUrls: ['./Wine-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Wine-card]': 'true'
  }
})

export class WineCardComponent {


}