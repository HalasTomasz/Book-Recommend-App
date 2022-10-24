import {createStore, combineReducers, applyMiddleware} from 'redux'
import thunk from 'redux-thunk'
import {composeWithDevTools} from 'redux-devtools-extension'
//import {bookListRedcurs, bookDataRedcurs} from './reducers/bookReducers'
//import {historyReducer} from './reducers/hisotryReducer'
//import {userRegisterReducer,userGetterReducer,userUpdateReducer } from './reducers/userReducer'

//const reducer = combineReducers({
//     bookList: bookListRedcurs,
//     bookData: bookDataRedcurs,
//     historyList: historyReducer,
//     userRegister: userRegisterReducer,
//     getUser: userGetterReducer,
//     updateUser:userUpdateReducer,
//})



const middleware = [thunk]

const store = createStore(
    composeWithDevTools(applyMiddleware(...middleware
    )) )

export default store
