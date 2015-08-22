var React = require('react');

var TasksList = require('./TasksList');

module.exports = React.createClass({
    render: function() {
        return (
            <div>
                <h2>Incomplete</h2>
                <TasksList tasks={this.props.tasks.filter(x => x.completed === false)} />
            </div>
        );
    }
});
