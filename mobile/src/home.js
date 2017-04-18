
/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */

import React, { Component } from 'react';
import {
  StyleSheet,
  Text,
  View,
  Image,
  TouchableHighlight,
  ToastAndroid,
  Button
} from 'react-native';
import Routes from './routes';
import settings from './settings';
import wifi from 'react-native-android-wifi';

const TIMER_COUNTER = 2 * 1000;
const MAX_COUNTER_TIMES = 5;
const SSID = 'HODOR';
const PASS = 'hodor2017';
const RECONNECTION_INTERVAL = 10;

const connectToHodorWifi = fn => {
  wifi.findAndConnect(SSID, PASS, found => {
    if(!found){
      return fn(new Error('hodor network not found'));
      // return setTimeout(() => connectToHodorWifi(fn), RECONNECTION_INTERVAL * 1000);
    }
    return fn(null);
  });
};

const enableNetwork = cb => {
  wifi.connectionStatus(isConnected => {
    if(!isConnected) {
      wifi.setEnabled(true);
      return setTimeout(() => connectToHodorWifi(cb), 1000);
    }
    wifi.getSSID((ssid) => {
      if(!ssid || ssid !== SSID) return connectToHodorWifi(cb);
      cb(null);
    });
  });
}

export default class HomeView extends Component {

  constructor(props){
    super(props);
  }

  componentDidMount(){
    enableNetwork((error)=>{
      if(error) return this._displayConnectionError();
      ToastAndroid.showWithGravity(
          `Connected to ${SSID} network`,
          ToastAndroid.LONG,
          ToastAndroid.BOTTOM)
    });
  }

  _displayConnectionError(){
    ToastAndroid.showWithGravity(
      `${SSID} network not found`,
      ToastAndroid.LONG,
      ToastAndroid.BOTTOM,
    );
  }

  _emit(action, onResponse){
    //console.warn(`http://${settings.host}:${settings.port}/${action}`)
    fetch(`http://${settings.host}:${settings.port}/${action}`, {method: 'GET'})
    .then(response => response.ok ? onResponse(null, response) : onResponse(new Error('Network response was not ok.')))
    .catch(error => onResponse(error));
  }

  join(){
    enableNetwork((error)=>{
      if(error) return this._displayConnectionError();
      this._emit('pi/join', (error, data) => console.log('joined'))
    });
  }

  leave(){
    enableNetwork((error)=>{
      if(error) return this._displayConnectionError();
      this._emit('pi/leave', (error, data) => console.log('left'));
    });
  }

  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.title}>HODOR</Text>
        <Text style={styles.description}>Opening your doors since <Text style={styles.year}>2016</Text></Text>
        <View style={styles.logoContainer}>
          <Image source={require('../img/logo.png')} style={styles.logo}/>
        </View>
        <View style={styles.buttonContainer}>
          <TouchableHighlight
            style={styles.button}
            onPress={this.leave.bind(this)}
            underlayColor='#494949'>
              <Text style={styles.textButton}>LEAVE</Text>
          </TouchableHighlight>
          <TouchableHighlight
            style={styles.button}
            onPress={this.join.bind(this)}
            underlayColor='#494949'>
              <Text style={styles.textButton}>JOIN</Text>
          </TouchableHighlight>
        </View>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'column',
    alignItems: 'center',
    backgroundColor: '#181818'
  },
  title: {
    fontSize: 35,
    textAlign: 'center',
    marginTop: 40,
    color: '#f1f1f1',
    fontFamily: 'throne'
  },
  description: {
    fontSize: 10,
    textAlign: 'center',
    marginTop: 5,
    color: '#f1f1f1',
    fontFamily: 'throne',
    opacity: 0.8
  },
  year:{
    fontSize: 14
  },
  logoContainer: {
    width: 120,
    height: 100,
    marginTop: 60,
    marginBottom: 5
  },
  logo: {
    flex: 1,
    width: null,
    height: null,
    resizeMode: 'contain'
  },
  button : {
    backgroundColor: '#181818',
    marginBottom: 60,
    borderRadius: 5,
    borderWidth: 0.5,
    borderColor: '#f1f1f1',
    width: 120,
    height: 40,
    paddingTop: 12
  },
  textButton: {
    color: "#f1f1f1",
    textAlign: 'center',
    fontFamily: 'throne'
  },
  buttonContainer: {
    flex: 1,
    flexDirection: 'column',
    justifyContent: 'flex-end',
    alignItems: 'center'
  }
});
