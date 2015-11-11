var React = require('react');


module.exports = React.createClass({
    render: function() {
        return (
            <ul>{ this.props.tasks.map((x, i) => 
                <li key={'todoitem' + i}>{x.description}</li>
            )}</ul>
        );
    }
});
