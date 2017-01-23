/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */

import React, { Component } from 'react';
import { Image } from 'react-native';
import { Container, Header, Title, Content, List, ListItem, Badge, Footer, FooterTab, Thumbnail, Text, Button, Icon } from 'native-base';

const HOST = '192.168.1.5';
const PORT = '8080';

export default class Parking extends Component {

  _emit(action, onResponse){
    // const response = await fetch(`http://${HOST}:${PORT}/${action}`, {method: 'GET'});
    // if(response.ok) onResponse(response);
    fetch(`http://${HOST}:${PORT}/${action}`, {method: 'GET'})
    .then(response => {
      if(response.ok) {
        return onResponse(response);
      }
      throw new Error('Network response was not ok.');
    })
    .catch(error => {
      console.error(error);
      throw new Error(error)
    });
  }

  join(){
    this._emit('pi/join', (data) => console.log('joined'));
  }

  leave(){
    this._emit('pi/leave', (data) => console.log('left'));
  }

  render() {
    return (
      <Container>
        <Header style={{backgroundColor: 'rgba(36, 37, 38, 1)'}}>
          <Button transparent>
              <Icon name='ios-menu' />
          </Button>
          <Title>Hodor</Title>
          <Button transparent>
              <Icon name='ios-settings' />
          </Button>
        </Header>
        <Content>
           <List>
               <ListItem>
                   <Thumbnail source={require('../img/play.png')} />
                   <Text>Alberto: Joined at ?</Text>
                   <Text note>Parking place till 10/02/2017</Text>
               </ListItem>
               <ListItem>
                 <Thumbnail source={require('../img/play.png')} />
                 <Text>Zuri: Left at ?</Text>
                 <Text note>Parking place till 10/02/2017</Text>
               </ListItem>
           </List>
        </Content>
        <Footer style={{backgroundColor: 'rgba(36, 37, 38, 1)'}}>
          <FooterTab>
            <Button transparent onPress={this.join.bind(this)}>
                <Icon name="ios-car" />
                Join
            </Button>
            <Button transparent onPress={this.leave.bind(this)}>
                <Icon name="ios-car-outline" />
                Leave
            </Button>
            <Button transparent>
                <Icon name="ios-beer-outline" />
                More
            </Button>
          </FooterTab>
        </Footer>
      </Container>
    );
  }
}
