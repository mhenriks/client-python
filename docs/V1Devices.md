# V1Devices

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoattach_graphics_device** | **bool** | Wheater to attach the default graphics device or not. VNC will not be available if set to false. Defaults to true. | [optional] 
**autoattach_pod_interface** | **bool** | Whether to attach a pod network interface. Defaults to true. | [optional] 
**disks** | [**list[V1Disk]**](V1Disk.md) | Disks describes disks, cdroms, floppy and luns which are connected to the vmi. | [optional] 
**interfaces** | [**list[V1Interface]**](V1Interface.md) | Interfaces describe network interfaces which are added to the vm. | [optional] 
**rng** | [**V1Rng**](V1Rng.md) | Whether to have random number generator from host +optional | [optional] 
**watchdog** | [**V1Watchdog**](V1Watchdog.md) | Watchdog describes a watchdog device which can be added to the vmi. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


