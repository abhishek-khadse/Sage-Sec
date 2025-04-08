import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"

export function Reports() {
  return (
    <div className="p-6 space-y-6">
      <h1 className="text-3xl font-bold">Reports</h1>
      <Card>
        <CardHeader>
          <CardTitle>Analysis Reports</CardTitle>
        </CardHeader>
        <CardContent>
          <p>Reports content will be implemented here.</p>
        </CardContent>
      </Card>
    </div>
  )
}