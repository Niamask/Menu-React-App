import { Link, useNavigate } from 'react-router-dom';
import PropTypes from 'prop-types';

function LinkButton({ children, to }) {
  const navigate = useNavigate();
  const className =
    'text-sm text-orange-500 hover:text-orange-600   hover:underline';

  if (to === '-1')
    return (
      <button className={className} onClick={() => navigate(-1)}>
        {children}
      </button>
    );

  return (
    <div>
      <Link to={to} className={className}>
        {children}
      </Link>
    </div>
  );
}

LinkButton.propTypes = {
  children: PropTypes.node.isRequired, // Can be any React element or node
  to: PropTypes.string, // Optional boolean prop
};

export default LinkButton;
