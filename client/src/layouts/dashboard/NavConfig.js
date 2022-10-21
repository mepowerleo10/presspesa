// component
import Iconify from '../../components/Iconify';

// ----------------------------------------------------------------------

const getIcon = (name) => <Iconify icon={name} width={22} height={22} />;

const navConfig = [
  {
    title: 'sharedDashboard',
    path: '/dashboard/app',
    icon: getIcon('eva:pie-chart-2-fill'),
  },
  {
    title: 'sharedAds',
    path: '/dashboard/ads',
    icon: getIcon('eva:file-text-fill'),
  },
  {
    title: 'sharedWithdrawals',
    path: '/dashboard/withdrawals',
    icon: getIcon('eva:credit-card-fill'),
  },
  {
    title: 'sharedNotFound',
    path: '/404',
    icon: getIcon('eva:alert-triangle-fill'),
  },
];

export default navConfig;
