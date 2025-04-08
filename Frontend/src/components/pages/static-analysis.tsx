import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"

export function StaticAnalysis() {
  return (
    <div className="p-6 space-y-6">
      <h1 className="text-3xl font-bold">Static Analysis</h1>
      <Card>
        <CardHeader>
          <CardTitle>Static Analysis Dashboard</CardTitle>
        </CardHeader>
        <CardContent>
          <p>Static analysis content will be implemented here.</p>
        </CardContent>
      </Card>
    </div>
  )
}