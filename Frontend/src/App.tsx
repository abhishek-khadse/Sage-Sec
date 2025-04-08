import { useState } from 'react';
import { ThemeProvider } from '@/components/theme-provider';
import { Toaster } from '@/components/ui/sonner';
import { MainLayout } from '@/components/layout/main-layout';
import { Dashboard } from '@/components/pages/dashboard';
import { StaticAnalysis } from '@/components/pages/static-analysis';
import { DynamicAnalysis } from '@/components/pages/dynamic-analysis';
import { NetworkBehavior } from '@/components/pages/network-behavior';
import { MLClassification } from '@/components/pages/ml-classification';
import { Reports } from '@/components/pages/reports';
import { Settings } from '@/components/pages/settings';
import { About } from '@/components/pages/about';

type Page = 'dashboard' | 'static' | 'dynamic' | 'network' | 'ml' | 'reports' | 'settings' | 'about';

function App() {
  const [currentPage, setCurrentPage] = useState<Page>('dashboard');

  const renderPage = () => {
    switch (currentPage) {
      case 'dashboard':
        return <Dashboard />;
      case 'static':
        return <StaticAnalysis />;
      case 'dynamic':
        return <DynamicAnalysis />;
      case 'network':
        return <NetworkBehavior />;
      case 'ml':
        return <MLClassification />;
      case 'reports':
        return <Reports />;
      case 'settings':
        return <Settings />;
      case 'about':
        return <About />;
      default:
        return <Dashboard />;
    }
  };

  return (
    <ThemeProvider defaultTheme="dark" storageKey="sage-sec-theme">
      <MainLayout currentPage={currentPage} onPageChange={setCurrentPage}>
        {renderPage()}
      </MainLayout>
      <Toaster />
    </ThemeProvider>
  );
}

export default App;