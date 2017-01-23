/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */
 import React, { Component } from 'react';
 import { AppRegistry, Navigator } from 'react-native';
 import Routes from './src/routes';
 import Settings from './src/settings';

export default class Hodor extends Component {

  constructor(props){
    super(props);
    this.state = {routes: Routes};
  }

  render() {
    return (
      <Navigator
      ref={component => this._navigator = component}
      initialRoute={this.state.routes.home}
      renderScene={(route, navigator) => {
        const RouteComponent = this.state.routes[route.id].component;
        return <RouteComponent {...route.props} navigator={navigator} />
        }
      }
      />
    );
  }
}

AppRegistry.registerComponent(Settings.appTitle, () => Hodor);

/*

import React, { Component } from 'react';
import {
  AppRegistry,
  StyleSheet,
  Text,
  View,
  Image
} from 'react-native';
import Button from 'react-native-button';
import _ from './paho.js';

const DEBUG = false;

class hodor extends Component {

  _onJoin(){

    console.log(Paho);

      connect("garage?join");
  }

  _onLeave(){

    connect("garage?leave");
  }

  render() {
    return (
      <View style={styles.container}>
        <Image
          source={require('./img/hodor.jpg')}
          style={styles.image}
        />
        <Text style={styles.instructions}>
          Please consider donating ;)
        </Text>
        <Button
          containerStyle={{padding:10, height:45, overflow:'hidden', borderRadius:4, backgroundColor: 'white'}}
          style={{fontSize: 20, color: 'rgba(0, 0, 0, 0.6)'}}
          onPress={this._onJoin}>
          Join
        </Button>
        <Button
          containerStyle={{padding:10, height:45, overflow:'hidden', borderRadius:4, backgroundColor: 'white'}}
          style={{fontSize: 20, color: 'rgba(0, 0, 0, 0.6)'}}
          onPress={this._onLeave}>
          Leave
        </Button>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
  instructions: {
    textAlign: 'center',
    color: '#333333',
    margin: 5,
  },
  image:{
    width: 400,
    height: 300
  },
  button: {
    width: 40,
    height: 40
  }
});

const connect = function (messageID){

  var hostname = 'iot.eclipse.org';
  var port = 80;
  var clientID = 'itrsgroup';
  var mqttID = DEBUG ? '' : 'com/itrsgroup/mlg2016';
  //var mqttID = 'test';
  var timer;

  // Create a client instance
  client = new Paho.MQTT.Client(hostname, port, clientID);


  // connect the client
  client.connect({

    onSuccess: function(){

      const message = new Paho.MQTT.Message(messageID);
      message.destinationName = mqttID;
      client.send(message);

      client.disconnect();

    }

  });

}


AppRegistry.registerComponent('hodor', () => hodor);

*/
