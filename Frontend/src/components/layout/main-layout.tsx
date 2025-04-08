import { useState } from 'react';
import { cn } from '@/lib/utils';
import { Button } from '@/components/ui/button';
import { ScrollArea } from '@/components/ui/scroll-area';
import { Sheet, SheetContent, SheetTrigger } from '@/components/ui/sheet';
import { useTheme } from '@/components/theme-provider';
import {
  ChevronRight,
  Menu,
  Home,
  FileSearch,
  Play,
  Network,
  Brain,
  FileText,
  Settings,
  Sun,
  Moon,
  Laptop,
  Info,
} from 'lucide-react';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu';

interface MainLayoutProps {
  children: React.ReactNode;
  currentPage: string;
  onPageChange: (page: any) => void;
}

const navigation = [
  { name: 'Dashboard', icon: Home, value: 'dashboard' },
  { name: 'Static Analysis', icon: FileSearch, value: 'static' },
  { name: 'Dynamic Analysis', icon: Play, value: 'dynamic' },
  { name: 'Network Behavior', icon: Network, value: 'network' },
  { name: 'ML Classification', icon: Brain, value: 'ml' },
  { name: 'Reports', icon: FileText, value: 'reports' },
  { name: 'Settings', icon: Settings, value: 'settings' },
  { name: 'About', icon: Info, value: 'about' },
];

export function MainLayout({ children, currentPage, onPageChange }: MainLayoutProps) {
  const [open, setOpen] = useState(false);
  const { theme, setTheme } = useTheme();

  return (
    <div className="flex min-h-screen">
      {/* Sidebar for desktop */}
      <div className="hidden lg:flex lg:w-72 lg:flex-col">
        <div className="flex grow flex-col gap-y-5 overflow-y-auto border-r border-gray-200 dark:border-gray-800 bg-gray-100/40 dark:bg-gray-900/40 px-6 pb-4">
          <div className="flex h-16 shrink-0 items-center">
            <FileSearch className="h-8 w-8" />
            <span className="ml-2 text-lg font-semibold">MRET</span>
          </div>
          <nav className="flex flex-1 flex-col">
            <ul role="list" className="flex flex-1 flex-col gap-y-7">
              <li>
                <ul role="list" className="-mx-2 space-y-1">
                  {navigation.map((item) => (
                    <li key={item.name}>
                      <Button
                        variant={currentPage === item.value ? 'secondary' : 'ghost'}
                        className={cn(
                          'w-full justify-start',
                          currentPage === item.value && 'bg-gray-200 dark:bg-gray-800'
                        )}
                        onClick={() => onPageChange(item.value)}
                      >
                        <item.icon className="mr-2 h-4 w-4" />
                        {item.name}
                      </Button>
                    </li>
                  ))}
                </ul>
              </li>
            </ul>
          </nav>
        </div>
      </div>

      {/* Mobile sidebar */}
      <Sheet open={open} onOpenChange={setOpen}>
        <SheetTrigger asChild>
          <Button
            variant="ghost"
            className="lg:hidden fixed left-4 top-4 z-40"
          >
            <Menu className="h-6 w-6" />
          </Button>
        </SheetTrigger>
        <SheetContent side="left" className="w-72 p-0">
          <ScrollArea className="h-full px-6">
            <div className="flex h-16 shrink-0 items-center">
              <FileSearch className="h-8 w-8" />
              <span className="ml-2 text-lg font-semibold">MRET</span>
            </div>
            <nav className="flex flex-1 flex-col">
              <ul role="list" className="flex flex-1 flex-col gap-y-7">
                <li>
                  <ul role="list" className="-mx-2 space-y-1">
                    {navigation.map((item) => (
                      <li key={item.name}>
                        <Button
                          variant={currentPage === item.value ? 'secondary' : 'ghost'}
                          className={cn(
                            'w-full justify-start',
                            currentPage === item.value && 'bg-gray-200 dark:bg-gray-800'
                          )}
                          onClick={() => {
                            onPageChange(item.value);
                            setOpen(false);
                          }}
                        >
                          <item.icon className="mr-2 h-4 w-4" />
                          {item.name}
                        </Button>
                      </li>
                    ))}
                  </ul>
                </li>
              </ul>
            </nav>
          </ScrollArea>
        </SheetContent>
      </Sheet>

      {/* Main content */}
      <div className="flex-1">
        <div className="sticky top-0 z-30 flex h-16 shrink-0 items-center gap-x-4 border-b border-gray-200 dark:border-gray-800 bg-gray-100/40 dark:bg-gray-900/40 px-4 shadow-sm sm:gap-x-6 sm:px-6 lg:px-8">
          <div className="flex flex-1 gap-x-4 self-stretch lg:gap-x-6">
            <div className="flex items-center gap-x-4 lg:gap-x-6">
              <span className="text-sm font-semibold leading-6">
                {navigation.find((item) => item.value === currentPage)?.name}
              </span>
            </div>
            <div className="flex flex-1 items-center justify-end gap-x-4">
              <DropdownMenu>
                <DropdownMenuTrigger asChild>
                  <Button variant="ghost" size="icon">
                    {theme === "light" && <Sun className="h-5 w-5" />}
                    {theme === "dark" && <Moon className="h-5 w-5" />}
                    {theme === "system" && <Laptop className="h-5 w-5" />}
                  </Button>
                </DropdownMenuTrigger>
                <DropdownMenuContent align="end">
                  <DropdownMenuItem onClick={() => setTheme("light")}>
                    <Sun className="mr-2 h-4 w-4" />
                    Light
                  </DropdownMenuItem>
                  <DropdownMenuItem onClick={() => setTheme("dark")}>
                    <Moon className="mr-2 h-4 w-4" />
                    Dark
                  </DropdownMenuItem>
                  <DropdownMenuItem onClick={() => setTheme("system")}>
                    <Laptop className="mr-2 h-4 w-4" />
                    System
                  </DropdownMenuItem>
                </DropdownMenuContent>
              </DropdownMenu>
            </div>
          </div>
        </div>

        <main className="p-4 sm:p-6 lg:p-8">
          {children}
        </main>
      </div>
    </div>
  );
}