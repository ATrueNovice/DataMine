import platform
from datetime import datetime
import socket
import uuid
import re
import psutil


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def System_information():
    x = []
    
    # Header
    uname = platform.uname()

    
    header ="="*40, "System Information", "="*40
    system = uname.system
    node =uname.node
    users = psutil.users()
    current_profile = psutil.use()
    release = uname.release
    version = uname.version
    machine = uname.machine
    processor=uname.processor
    
    mac_address = f"{':'.join(re.findall('..', '%012x' % uuid.getnode()))}"
    # print(header)
    
    x.append(f"{header}\n")
    x.append(f"System: {system}\n")
    x.append(f"Node Name:  {node}\n")
    x.append(f"Users:  {users}\n")
    x.append(f"Release: {release}\n")
    x.append(f"Version: {version}\n")
    x.append(f"Machine: {machine}\n")
    x.append(f"Processor: {processor}\n")
    x.append(f"Mac Address: {mac_address}\n")
    z = f" {''.join(x)}"

    # print(f"Processor: {cpuinfo.get_cpu_info()['brand_raw']}")
    # print(f"Ip-Address: {socket.gethostbyname(socket.gethostname())}")



    # Boot Time
    boot_time_timestamp = psutil.boot_time()
    boot_data = []
    bheader = "="*40, "Boot Time", "="*40
    bt = datetime.fromtimestamp(boot_time_timestamp)
    boot_info = f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"

    boot_data.append(f'{bheader}\n')
    boot_data.append(f'{boot_info}\n')
    boots_data = f" {''.join(boot_data)}\n"
    # print(boot_data)
    
    cpu_data = []
    cpu_header = "="*40, "CPU Info", "="*40
    pcores = psutil.cpu_count(logical=False)
    tcores = psutil.cpu_count(logical=True)
    cpufreq = psutil.cpu_freq()

    cpu_data.append(f'{cpu_header}\n')
    cpu_data.append(f'Physical Cores: {pcores}\n')
    cpu_data.append(f'Total Cores: {tcores}\n')
    cpu_data.append(f"Max Frequency: {cpufreq.max:.2f}Mhz \n")
    cpu_data.append(f"Min Frequency: {cpufreq.min:.2f}Mhz \n")
    cpu_data.append(f"Current Frequency: {cpufreq.current:.2f}Mhz\n")
    cpu_data.append(f"Current Frequency: {cpufreq.current:.2f}Mhz\n")
    cpu_data.append("CPU Usage Per Core: \n")
    cpu_data.append(f"Current Frequency: {cpufreq.current:.2f}Mhz\n")
    
    
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        cpu_data.append(f"Core {i}: {percentage}% \n")

    # print(f"Total CPU Usage: {psutil.cpu_percent()}%")
    cpu_data.append(f"Total CPU Usage: {psutil.cpu_percent()}%")

    # print(f" {''.join(cpu_data)} \n")

   



    mem = []
    mem_banner = "="*40, "Memory Information", "="*40
    svmem = psutil.virtual_memory()

    mem.append(f"{mem_banner}\n")
    mem.append(f"Total: {get_size(svmem.total)}\n")
    mem.append(f'Available: {get_size(svmem.available)}\n')
    mem.append(f'"Used: {get_size(svmem.used)}\n')
    mem.append(f'Percentage: {svmem.percent}%\n')
    # print(f" {''.join(mem)} \n")
    

    # mem.append(f'{}\n')
    # Memory Information
    # print("="*40, "Memory Information", "="*40)
    # get the memory details
    # print(f"Total: {get_size(svmem.total)}")
    # print(f"Available: {get_size(svmem.available)}")
    # print(f"Used: {get_size(svmem.used)}")
    # print(f"Percentage: {svmem.percent}%")


    swap_data = []
    swap = psutil.swap_memory()

    swap_header = "="*20, "SWAP", "="*20
    swap_data.append(f'{swap_header}\n')
    swap_data.append(f'Total: {get_size(swap.total)}\n')
    swap_data.append(f'Free: {get_size(swap.free)}\n')
    swap_data.append(f'Used: {get_size(swap.used)}\n')
    swap_data.append(f'Percentage: {swap.percent}%\n')
    # print(f" {''.join(swap_data)} \n")

    # print("="*20, "SWAP", "="*20)
    # # get the swap memory details (if exists)
    # print(f"Total: {get_size(swap.total)}")
    # print(f"Free: {get_size(swap.free)}")
    # print(f"Used: {get_size(swap.used)}")
    # print(f"Percentage: {swap.percent}%")


    disc_data = []
    partitions = psutil.disk_partitions()

    disc_header = "="*40, "Disk Information", "="*40
    disc_data.append(f'Percentage: {disc_header}%\n')
    disc_data.append(f'Partitions and Usage:\n')
    for partition in partitions:
        disc_data.append(f"=== Device: {partition.device} ===\n")
        disc_data.append(f"  Mountpoint: {partition.mountpoint}\n")
        disc_data.append(f"  File system type: {partition.fstype}\n")
        # disc_data.append(f"=== Device: {partition.device} ===\n")

        # print(f"=== Device: {partition.device} ===")
        # print(f"  Mountpoint: {partition.mountpoint}")
        # print(f"  File system type: {partition.fstype}")
        try:

            partition_usage = psutil.disk_usage(partition.mountpoint)
            disc_data.append(f"=== Partition Usage: {partition_usage} ===\n")

        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            continue
        disc_data.append(f"  Total Size: {get_size(partition_usage.total)}\n")
        disc_data.append(f"  Used: {get_size(partition_usage.used)}\n")
        disc_data.append(f"  Free: {get_size(partition_usage.free)}\n")
        disc_data.append(f"  Percentage: {partition_usage.percent}%\n")

        # print(f"  Total Size: {get_size(partition_usage.total)}")
        # print(f"  Used: {get_size(partition_usage.used)}")
        # print(f"  Free: {get_size(partition_usage.free)}")
        # print(f"  Percentage: {partition_usage.percent}%")
    # get IO statistics since boot
    disk_io = psutil.disk_io_counters()
    disc_data.append(f"Total read: {get_size(disk_io.read_bytes)}\n")
    disc_data.append(f"Total write: {get_size(disk_io.write_bytes)}\n")

    # print(f"Total read: {get_size(disk_io.read_bytes)}")
    # print(f"Total write: {get_size(disk_io.write_bytes)}")


    partitions = psutil.disk_partitions()
    for partition in partitions:
        disc_data.append(f'=== Device: {partition.device} ===\n')
        disc_data.append(f'  Mountpoint: {partition.mountpoint}\n')
        disc_data.append(f'  File system type: {partition.fstype}\n')

        # print(f"=== Device: {partition.device} ===")
        # print(f"  Mountpoint: {partition.mountpoint}")
        # print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            continue
        
        disc_data.append(f'  Total Size: {get_size(partition_usage.total)}\n')
        disc_data.append(f'  Used: {get_size(partition_usage.used)}')
        disc_data.append(f'  Free: {get_size(partition_usage.free)}\n')
        disc_data.append(f'  Percentage: {partition_usage.percent}%\n')

        # print(f"  Total Size: {get_size(partition_usage.total)}")
        # print(f"  Used: {get_size(partition_usage.used)}")
        # print(f"  Free: {get_size(partition_usage.free)}")
        # print(f"  Percentage: {partition_usage.percent}%")
    # get IO statistics since boot
    disk_io = psutil.disk_io_counters()
    disc_data.append(f'Total read: {get_size(disk_io.read_bytes)}\n')
    disc_data.append(f'Total write: {get_size(disk_io.write_bytes)}\n')

    # print(f"Total read: {get_size(disk_io.read_bytes)}")
    # print(f"Total write: {get_size(disk_io.write_bytes)}")
    
    
    # print(f" {''.join(disc_data)} \n")


    # Disk Information
    # print("="*40, "Disk Information", "="*40)
    # print("Partitions and Usage:")
    # get all disk partitions


    network_banner = []
    network_info = "="*40, "Network Information", "="*40
    network_banner.append(f'Network: {network_info} \n')
    # network_banner.append(f'=== Interface: {interface_name} ===\n')
    # network_banner.append(f'Total write: {get_size(disk_io.write_bytes)}\n')

    ## Network information
    # print("="*40, "Network Information", "="*40)
    ## get all network interfaces (virtual and physical)
    
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            # network_banner.append(f'=== Interface: {interface_name} ===\n')

            # print(f"=== Interface: {interface_name} ===")
            banner = f'=== Interface: {interface_name} ===\n'
            network_banner.append(banner)

            if str(address.family) == 'AddressFamily.AF_INET':
                interface_banner = f'=== Interface: {interface_name} ===\n'
                network_banner.append(interface_banner)
                network_banner.append(f'  IP Address: {address.address}\n')
                network_banner.append(f'  Netmask: {address.netmask}\n')
                network_banner.append(f'  Broadcast IP: {address.broadcast}\n')

                # print(f"  IP Address: {address.address}")
                # print(f"  Netmask: {address.netmask}")
                # print(f"  Broadcast IP: {address.broadcast}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                network_banner.append(f'  MAC Address: {address.address}\n')
                network_banner.append(f'  Netmask: {address.netmask}\n')
                network_banner.append(f'  Broadcast IP: {address.broadcast}\n')

                # print(f"  MAC Address: {address.address}")
                # print(f"  Netmask: {address.netmask}")
                # print(f"  Broadcast MAC: {address.broadcast}")
                
    # import pdb; pdb.set_trace()    
    # print(f" {''.join(network_banner)} \n")

    ##get IO statistics since boot
    net_io = psutil.net_io_counters()
    end_counter = []
    end_counter.append(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}\n")
    end_counter.append(f"Total Bytes Received: {get_size(net_io.bytes_recv)}\n")
    
    ec_data = "="*40, "End Information", "="*40
    end_counter.append(f'  {ec_data}')
    
    # print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
    # print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
    # print("="*40, "End Information", "="*40)
    
    # print(boot_data)
    # print(z)    
    # print(f" {''.join(cpu_data)} \n")
    # print(f" {''.join(mem)} \n")
    # print(f" {''.join(swap_data)} \n")
    # print(f" {''.join(disc_data)} \n")
    # print(f" {''.join(network_banner)} \n")

    data = f" {''.join(end_counter)} \n"
    # print(data)
    final_results = []
    final_results.append(boots_data)
    final_results.append(z)
    final_results.append(f" {''.join(cpu_data)} \n")
    final_results.append(f" {''.join(mem)} \n")
    final_results.append(f" {''.join(swap_data)} \n")
    final_results.append(f" {''.join(disc_data)} \n")
    final_results.append(f" {''.join(network_banner)} \n")
    final_results.append(f" {''.join(end_counter)} \n")
    xboots_data = f" {''.join(final_results)}\n"
    # print(xboots_data)
    # output(xboots_data)
    with open(f'AMC_{node}.txt', 'w') as f:
        
        f.write(xboots_data)
        f.write('\n')
if __name__ == "__main__":

    System_information()


def output(data):
    lines = System_information()
    # f = open(path_to_file, mode)
    with open('test.txt', 'w') as f:
        
        f.write(data)
        f.write('\n')
# output()