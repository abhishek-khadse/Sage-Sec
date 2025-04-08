import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Progress } from '@/components/ui/progress';
import {
  Shield,
  AlertTriangle,
  FileWarning,
  Activity,
  Loader2,
} from 'lucide-react';

// Sample data - replace with real data from your backend
const stats = [
  {
    name: 'Total Scans',
    value: '1,234',
    icon: Shield,
    description: 'Last 30 days',
  },
  {
    name: 'Threats Found',
    value: '89',
    icon: AlertTriangle,
    description: 'High severity threats',
  },
  {
    name: 'Files Analyzed',
    value: '2,845',
    icon: FileWarning,
    description: 'Across all scans',
  },
  {
    name: 'Active Scans',
    value: '3',
    icon: Activity,
    description: 'Currently processing',
  },
];

const recentScans = [
  {
    id: 1,
    name: 'suspicious_file.exe',
    progress: 100,
    status: 'completed',
    threat: 'high',
  },
  {
    id: 2,
    name: 'update_patch.msi',
    progress: 100,
    status: 'completed',
    threat: 'low',
  },
  {
    id: 3,
    name: 'system32.dll',
    progress: 65,
    status: 'scanning',
    threat: 'unknown',
  },
];

export function Dashboard() {
  return (
    <div className="space-y-6">
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        {stats.map((stat) => (
          <Card key={stat.name}>
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium">
                {stat.name}
              </CardTitle>
              <stat.icon className="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">{stat.value}</div>
              <p className="text-xs text-muted-foreground">
                {stat.description}
              </p>
            </CardContent>
          </Card>
        ))}
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Recent Scans</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            {recentScans.map((scan) => (
              <div
                key={scan.id}
                className="flex items-center space-x-4"
              >
                <div className="flex-1 space-y-1">
                  <p className="text-sm font-medium leading-none">
                    {scan.name}
                  </p>
                  <div className="flex items-center pt-2">
                    <Progress
                      value={scan.progress}
                      className="h-2"
                    />
                    {scan.status === 'scanning' && (
                      <Loader2 className="ml-2 h-4 w-4 animate-spin" />
                    )}
                  </div>
                </div>
                <div
                  className={`rounded-full px-2 py-1 text-xs font-semibold ${
                    scan.threat === 'high'
                      ? 'bg-red-100 text-red-700 dark:bg-red-900/30'
                      : scan.threat === 'low'
                      ? 'bg-green-100 text-green-700 dark:bg-green-900/30'
                      : 'bg-gray-100 text-gray-700 dark:bg-gray-800'
                  }`}
                >
                  {scan.threat}
                </div>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>
    </div>
  );
}