var React = require('react');


module.exports = React.createClass({
    render: function() {
        return (
            <ul>
                {
                    this.props.tasks.map(x => <li>{x.description}</li>)
                }
            </ul>
        );
    }
});
