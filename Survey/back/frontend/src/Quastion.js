import React from "react";
import {StylesManager, Model} from "survey-core";
import {Survey, PopupSurvey } from "survey-react-ui";
import { FunctionFactory } from "survey-core";
import "survey-core/defaultV2.css";
import "./index.css";
import {json} from "./json"
import {dicts} from "./dict"
import {dicts2} from "./dicts2"
import {useDispatch } from 'react-redux'
import { registerReview } from "./bookAction";

StylesManager.applyTheme("defaultV2");


function rowsWithValue(params) {

    if (! params && params.length === 3) 
        return false;

    var matrixValue = params[0];
    var rowCount = 0;
    for (var key in matrixValue) {
        rowCount++;
    }

    return rowCount;
  }

function setName(params) {

  var rating = params[0];
  var books = params[1];
  var survey = this.survey;
  const tmp = []
  for (let i = 0; i < books.length; i++){
    tmp.push(dicts[books[i]] + '\n' + '------------------------' + '\n')
  }
  console.log(params)
  survey[rating] = 'display'
  survey.setValue(rating, tmp);
}

function setName2(params) {

  var rating = params[0];
  var books = params[1];
  var survey = this.survey;
  const tmp = []
  for (let i = 0; i < books.length; i++){
    tmp.push(dicts2[books[i]]+ '\n' + '------------------------' + '\n')
  }
  console.log(params)
  survey[rating] = 'display'
  survey.setValue(rating, tmp);
}


FunctionFactory.Instance.register("setName", setName);
FunctionFactory.Instance.register("rowsWithValue", rowsWithValue);
FunctionFactory.Instance.register("setName2", setName2);

function Quastion() {
    

  const survey = new Model(json);
  const dispatch = useDispatch()

  function senderfun(sender){
    dispatch(registerReview(sender.data.algo1, sender.data.algo2,  sender.data.books))
    }


  survey.onComplete.add(function (sender, options) { // kill the timer
    // save the data on survey complete. You may call another function to store the final results
    senderfun(sender)
   //const fileData = JSON.stringify(sender.data)
  });
  // Render the survey inside the page
  return <Survey model={survey} />;

}
export default Quastion;