var React = require('react');

var Incomplete = require('./Incomplete');
var Completed = require('./Completed');

module.exports = React.createClass({
    getInitialState:  function() {
        return {
            tasks: []
        };
    },
    componentDidMount: function() {
        // call ajax here
        this.setState({
            tasks: 
           [
        {
            "url": "http://127.0.0.1:8000/api/tasks/1/",
            "description": "Buy milk",
            "completed": true,
            "due_time": "2017-03-02T01:04:00Z",
            "date_edited": "2015-08-19T12:30:29.754435Z"
        },
        {
            "url": "http://127.0.0.1:8000/api/tasks/2/",
            "description": "Buy chocolate",
            "completed": false,
            "due_time": null,
            "date_edited": "2015-08-19T12:31:45.809334Z"
        }
    ] 
        });
    },
    render: function() {
        return (
            <div>
                <h1>Todo List</h1>
                <Incomplete tasks={this.state.tasks} />
                <Completed tasks={this.state.tasks} />
            </div>
        );
    }
});

