import {createStore, combineReducers, applyMiddleware} from 'redux'
import thunk from 'redux-thunk'
import {composeWithDevTools} from 'redux-devtools-extension'
import {ReviewrReducer} from './bookReducers'

const reducer = combineReducers({
    NewReview: ReviewrReducer,

})

const middleware = [thunk]
const store = createStore( reducer,
    composeWithDevTools(applyMiddleware(...middleware
    )) )

export default store
