/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */

import HomeView from './login';
import ParkingView from './parking';

export default {
  home: {
    id: 'home',
    title: 'Home',
    component: HomeView
  },
  parking: {
    id: 'parking',
    title: 'Parking',
    component: ParkingView
  }
}
