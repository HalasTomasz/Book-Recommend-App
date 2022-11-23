import {
    REVIEW_ADD_REQUEST, 
    REVIEW_ADD_SUCESS, 
    REVIEW_ADD_FAIL,
} from './bookConstans'

export const ReviewrReducer = (state = {}, action) => {
    switch (action.type) {
        case REVIEW_ADD_REQUEST:
            return { loading: true }

        case REVIEW_ADD_SUCESS:
            return { loading: false, user_new: action.payload }

        case REVIEW_ADD_FAIL:
            return { loading: false, error: action.payload }
        default:
            return state
    }
}
