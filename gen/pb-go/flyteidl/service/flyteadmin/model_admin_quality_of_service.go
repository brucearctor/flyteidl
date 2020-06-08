/*
 * flyteidl/service/admin.proto
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * API version: version not set
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */

package flyteadmin
// AdminQualityOfService : This general categorization specifies how much queue time an execution can tolerate.  This can be extended in the future to make other execution-time decisions.   - QUALITY_OF_SERVICE_HIGH: Guarantees that this execution will begin as soon as requested and incur no queueing time.  - QUALITY_OF_SERVICE_MEDIUM: This execution may incur some queueing delay (e.g. 30 minutes) and is medium priority.  - QUALITY_OF_SERVICE_LOW: This execution may incur significant queueing delay (e.g. 2 hours) and is low priority.
type AdminQualityOfService string

// List of adminQualityOfService
const (
	AdminQualityOfServiceHIGH AdminQualityOfService = "QUALITY_OF_SERVICE_HIGH"
	AdminQualityOfServiceMEDIUM AdminQualityOfService = "QUALITY_OF_SERVICE_MEDIUM"
	AdminQualityOfServiceLOW AdminQualityOfService = "QUALITY_OF_SERVICE_LOW"
)
