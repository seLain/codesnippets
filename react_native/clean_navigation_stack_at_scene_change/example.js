import React, { Component } from 'react';
import CleanNavigator from './Utils.js';

class ExampleScene extends Component {

  onLogout(){
  	/*   rediret to login page */
    CleanNavigator.resetNavigation(this, 'LoginScene', {});
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