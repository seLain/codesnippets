import React, { Component } from 'react';
import CleanNavigator from './Utils.js';

class ExampleScene extends Component {

  onLogout(){
  	/*   logout alert  */
    Alert.alert(
      'Logout Alert',
      'Sure to logout ?',
      [
        {text: 'OK', onPress: () => { 
            console.log('OK Pressed'); 
            /*   rediret to login page */
            CleanNavigator.resetNavigation(this, 'LoginScene', {});
        }},
        {text: 'Cancel', onPress: () => console.log('Cancel Pressed'), style: 'cancel'},
      ],
      { cancelable: false }
    )
  }

  render() {
  	return (
      <View style={styles.container}>
          <Button onPress={this.onLogout.bind(this)}
                  title='Logout' />
      </View>
  	);
  }
}

module.exports = ExampleScene;