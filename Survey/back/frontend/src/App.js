import React from "react";
import Quastion from "./Quastion";
import { Provider } from 'react-redux';
import store from './store'


function App() {
  return (
    <Provider store={store}>
      <Quastion />
    </Provider>
  );
}

export default App;
